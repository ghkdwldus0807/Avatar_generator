import cv2, dlib
import numpy as np
from keras.models import load_model

age_list = [
    "(0, 2)",
    "(4, 6)",
    "(8, 12)",
    "(15, 20)",
    "(25, 32)",
    "(38, 43)",
    "(48, 53)",
    "(60, 100)",
]
gender_list = ["Male", "Female"]
detector = dlib.get_frontal_face_detector()


# age_net.caffemodel의 경로를 사용자의 local 경로에 맞게 다시 지정해주세요
age_net_url = r"D:\2023_2\OpenSourceSoftware\Avatar_generator\model\age_net.caffemodel"
# deploy_age.prototxt의 경로를 사용자의 local 경로에 맞게 다시 지정해주세요
age_net_protourl = (
    r"D:\2023_2\OpenSourceSoftware\Avatar_generator\model\deploy_age.prototxt"
)


# gender_net.caffemodel의 경로를 사용자의 local 경로에 맞게 다시 지정해주세요
gender_net_url = (
    r"D:\2023_2\OpenSourceSoftware\Avatar_generator\model\gender_net.caffemodel"
)
# deploy_gender.prototxt의 경로를 사용자의 local 경로에 맞게 다시 지정해주세요
gender_net_protourl = (
    r"D:\2023_2\OpenSourceSoftware\Avatar_generator\model\deploy_gender.prototxt"
)

# dog_cat_classify.model의 경로를 사용자의 local 경로에 맞게 다시 지정해주세요
model_path = (
    r"D:\2023_2\OpenSourceSoftware\Avatar_generator\model\dog_cat_classify.model"
)

# OPEN AI API KEY를 붙여넣어 주세요! 자세한 내용은 github를 참고해주세요
YOUR_API_KEY = "your_api_key"

# 아바타를 만들기 원하는 사진의 경로를 지정해주세요
img = cv2.imread(r"D:\2023_2\OpenSourceSoftware\Avatar_generator\img\img3.jpg")

# ---------------사용자의 로컬 환경에 맞는 경로 설정을 꼭 해주신 후 실행 하세요-------------------


age_net = cv2.dnn.readNetFromCaffe(age_net_protourl, age_net_url)
gender_net = cv2.dnn.readNetFromCaffe(gender_net_protourl, gender_net_url)
faces = detector(img)

for face in faces:
    x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
    face_img = img[y1:y2, x1:x2].copy()
    blob = cv2.dnn.blobFromImage(
        face_img,
        scalefactor=1,
        size=(227, 227),
        mean=(78.4263377603, 87.7689143744, 114.895847746),
        swapRB=False,
        crop=False,
    )
    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = gender_list[gender_preds[0].argmax()]
    print(gender)
    age_net.setInput(blob)
    age_preds = age_net.forward()
    age = age_list[age_preds[0].argmax()]
    print(age)


model = load_model(model_path)
img = cv2.resize(img, (64, 64))
img = img.astype("float32") / 255

img = np.expand_dims(img, axis=0)

prediction = model.predict(img)

animal = ""

if prediction[0][0] > 0.525:
    animal = "dog"
    print(animal)
else:
    animal = "cat"
    print(animal)

if animal == "dog":
    face = "lovely and sweet"
else:
    face = "haughty but charming"

# 안경 착용 여부 확인
while True:
    glasses = input("Is your avatar wearing glasses? (y (glasses)/ n (no glasses!)) : ")
    if glasses == "y" or glasses == "Y":
        glasses = "with eye-glasses"
        break
    elif glasses == "n" or glasses == "N":
        glasses = ""
        break
    else:
        print("Enter y or n !!")


from openai import OpenAI

client = OpenAI(api_key=YOUR_API_KEY)

response = client.images.generate(
    model="dall-e-3",
    prompt="Draw me a"
    + face
    + " Memoji style avatar that is "
    + gender
    + ", ages "
    + age
    + glasses,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)
