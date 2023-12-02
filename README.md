# 😎Avatar_generator
21101989 황지연

## 📚프로젝트 소개 
이 프로젝트는 사용자의 얼굴 사진을 분석하여 닮은 아바타를 생성하는 오픈 소스 소프트웨어입니다. OpenAI API를 이용하여 아바타 생성 기능을 제공합니다.


## 🌟프로젝트를 시작하기 전 주의 사항
1. 이 프로젝트는 anaconda 환경에서 제작되었습니다. 따라서 실행 또한 anaconda로 하시는 것을 추천합니다.
2. 이 프로젝트는 OpenAI API를 사용하는 프로젝트 입니다. 따라서 개인의 API KEY를 발급 받으시길 바랍니다.  
   [OPENAI API KEY 발급받는 법](https://www.daleseo.com/chatgpt-api-keys/)
3. 이 아바타 생성기는 한 명의 인물 사진이 들어왔을 때 유의미한 동작을 합니다. 따라서, 여러명의 사진은 지양해주세요.
4. 이 아바타 생성기는 OPEN AI API의 이미지 생성기 DELL-E-3을 기반으로 하기 때문에, 똑같은 사진으로 여러 번 코드를 실행하였을 때, 다른 결과가 나올 가능성이 큽니다. 그 점 양해부탁드립니다. 

## 🖥️프로젝트 실행 방법 (Windows)
1. Anaconda prompt를 관리자 권한으로 실행하여, 아래의 라이브러리들을 설치합니다.
```
pip install --upgrade openai
pip install cmake
pip install opencv-contrib-python dlib
```
(만약 pip install opencv-contrib-python dlib 단계에서 오류가 발생한다면, 해당 코드를 다시 입력해보세요.대부분 설치가 성공적으로 완료됩니다.)

2. **source, data 폴더 및  main_model.ipynb 파일을 제외한** github에 올려져 있는 파일을 모두 다운 받으세요.
3. **main.py** 파일을 엽니다.
4. main.py의 주석 내용을 참고하여 사용자의 LOCAL 환경에 맞게 **Model들의 경로를 재지정**해주시고, **발급받은 OPEN AI API KEY**도 붙여넣어주세요.
5. 그리고 아바타를 생성하길 원하는 사진도 img 경로에 지정해주세요
6. main.py를 실행합니다. 실행이 성공적으로 완료되면, 터미널에 뜨는 설명을 따라주세요
7. 마침내 생성된 아바타의 이미지 URL이 터미널에 뜬다면, 아바타 생성에 성공하신 것입니다 😊😊

---------
## 😄DEMO & EXAMPLE 

프로젝트가 성공적으로 실행되면 Terminal에 아래와 같은 질문이 뜹니다.
```
"Is your avatar wearing glasses? (y (glasses)/ n (no glasses!)) : "
```
원하는 답변을 선택하시면 아래에 생성된 아바타의 사진 링크가 제공됩니다. 클릭하시면 아바타의 사진이 뜹니다!  
![title](https://github.com/ghkdwldus0807/Avatar_generator/blob/main/source/howtouselink.png?raw=true)   

아래는 BLACKPINK의 JENNIE의 사진을 이용하여 아바타를 생성한 예시입니다. (실제 생성된 아바타의 링크에는 오른쪽 아바타의 사진만 뜹니다.)

![title](https://github.com/ghkdwldus0807/Avatar_generator/blob/main/source/example.png?raw=true)   

-----------

## 🗝️Models 

이 프로젝트는 두 가지 주요 모델을 사용하여 자신만의 아바타를 생성합니다. 첫 번째는 age_gender_model로, 이 모델은 제공된 이미지에서 인물의 나이와 성별을 판별합니다. 이 정보는 아바타 생성 과정에서 중요한 역할을 합니다. 두 번째 모델인 dog_cat_classifier는 사용자의 전체적인 이미지와 특성을 분석합니다.

이 프로젝트의 우리가 외모를 강아지나 고양이와 같은 동물의 특성으로 묘사하는 관습에서 착안했습니다. 이를 바탕으로, 만약 dog_cat_classifier 모델이 사용자를 '강아지상'으로 분류한다면, 이를 '사랑스럽고 달콤한(Lovely and Sweet)' 특성으로 변환합니다. 반면 '고양이상'으로 분류되면 '오만하지만 매력적인(Haughty but Charming)' 특성으로 변환하여 OpenAI API에 입력합니다. 이렇게 변환된 특성들은 최종 아바타 생성에 영향을 주어, 각 사용자에게 맞춤화된, 개성 넘치는 아바타를 제공합니다.

### 🐶😺dog_cat_classifier

1. Kaggle의 "Animal Faces" Dataset을 활용해 학습하였습니다. 해당 dataset에는 dog와 cat 이외의 wild라는 폴더의 dataset도 있지만, 해당 모델을 학습시킬 때에는 dog, cat의 데이터만 이용하였습니다.   
   Dataset 출처 : [Kaggle 'Animal Faces'](https://www.kaggle.com/datasets/andrewmvd/animal-faces/data)
2. Keras를 이용해 CNN 구조를 만들었습니다.   
![title](https://github.com/ghkdwldus0807/Avatar_generator/blob/main/source/dog_cat_classifier_model_accuracy.png?raw=true)



### 💞age_gender_model 

1. age_gender_model은 사전에 학습된 model을 사용하였습니다. model의 출처는 아래와 같습니다.
   https://github.com/GilLevi/AgeGenderDeepLearning/tree/master

-----------

## References 
References는 아래와 같습니다.   
https://gatherhere.tistory.com/14?category=863933   
https://lsjsj92.tistory.com/387   





