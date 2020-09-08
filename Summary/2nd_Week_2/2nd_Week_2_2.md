## 2주차 - 2. JSON 직렬화 - Serializer
 
 ### Model Form
 아래와 같은 `django`내부에 구현된 `forms`를 사용했었다.<br/>
 ```python
 from django import forms
 from .models import Blog
 
 class NewBlog(forms.ModelForm):
     class Meta:
         model = Blog
         fields = ['title', 'body']
 ```

|      Django      |    Django Rest Framework    |
|:----------------:|:---------------------------:|
| Form / ModelForm | Serializer / ModelSerializer |
|  **HTML Form**   |       **JSON 문자열**       |

#### 기능
1. `Model`로부터 `Field`를 읽어온다.<br/>
2. **유효성 검사**를 한다.

두개의 기능은 서로 매우 **유사**하다.<br/>
 
 ### Django vs Django Rest Framework
 
|                  |     Django      | Django Rest Framework |
|:----------------:|:---------------:|:---------------------:|
|  만들어지는 것   | 웹 어플리케이션 |      RESTful API      |
| 전달하는 데이터  | HTML / CSS / JS |      JSON 데이터      |
| 데이터를 담는 곳 |    **Form**     |    **Serializer**     | 

#### 공통점
- (모델로부터) **Field**를 **생성**
- **전송 가능 형식** (HTML Form / JSON 문자열)으로 만든다.
- 유효성 검사

### Serializer vs ModelSerializer
**Form**과 **ModelForm**이 존재하듯이 **Model**만 작성할 줄 알면<br/>
더 간편하게 **Serializer**를 사용할 수 있게하는 **ModelSerializer**에 대해서 공부한다.<br/>
**ModelSerializer**는 **쿼리셋**과 **모델 직렬화**를 알아서 해준다.<br/>
