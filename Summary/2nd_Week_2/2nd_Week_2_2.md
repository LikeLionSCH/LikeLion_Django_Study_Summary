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

|      Djagno      |    Django Rest Framework    |
|:----------------:|:---------------------------:|
| Form / ModelForm | Serializer / ModelSerialier |
|  **HTML Form**   |       **JSON 문자열**       |

#### 기능
1. `Model`로부터 `Field`를 읽어온다.<br/>
2. **유효성 검사**를 한다.

두개의 기능은 서로 매우 **유사**하다.<br/>
 
 ### Django vs Django Rest Framework
|                 |     Django      | Django Rest Framework |
|:---------------:|:---------------:|:---------------------:|
| 전달하는 데이터 | HTML / CSS / JS | JSON 데이터           |
|                 |                 |                       |
