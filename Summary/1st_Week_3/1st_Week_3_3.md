## 3주차 - 3.queryset & method
`DataBase`의 데이터를 `template`에 출력하기 위해 `views.py`이용

### 1. models.py의 class를 import
```python
from .models import Blog
```

### 2. views.py에 함수 정의
`models.py`로 부터 전달 받은 객체 목록(**쿼리셋**) 이용<br/>
```python
쿼리셋 = <클래스 이름>.objects
```

`DataBase`로 부터 받은 데이터를 활용(**메소드**)
```python
def home(request):
    blogs = Blog.objects

    return render(request, 'home.html', {
        'blogs': blogs,
    })
```

### 3. url 연결
이전에 진행했던 부분이라 설명은 생략
```python
from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
]
```

### 4. 쿼리셋 메소드 사용으로 데이터 출력
**쿼리셋과 메소드의 형식**<br/>
`model.objects.method()`<br/>

**예시**<br/>
`objects.all` : 모든 쿼리셋 반환<br/>
`objects.count` : 객체의 개수 반환<br/>
`objects.first` : 첫 번째 객체 반환<br/>
`objects.last` : 마지막 객체 반환

`all`메소드를 사용해 모든 **쿼리셋**을 가져와<br/>
**템플릿 코드**를 이용해 `for loop`을 진행하며<br/>
각 `object`의 데이터 `html`에 출력
```python
{% for blog in blogs.all %}
    <h1> {{ blog.title }} </h1>
    <p> {{ blog.pub_date }} </p>
    <p> {{blog.body }} </p>
    <br/>
    <br/>
{% endfor %}
```
