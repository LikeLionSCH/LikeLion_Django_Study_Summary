## 4주차 - 4. blog project 2

### 해야할 것
1. Navbar에 글쓰기 항목 만들기
2. 글쓰기 항목에 `url` 연결하기
3. 데이터 입력 공간 생성 및 제출 버튼 기능 구현(`views.py`)하기
    + `request`가 들어오면 `new.html`을 띄우는 함수
    + `new.html`에서 입력한 내용을 `DB`에 등록하는 함수

### 1. new.html 구성
다음과 같이 `new.html`을 구성
```html
<div class="container">
    <form action="">
        <h4>제목</h4>
        <input type="text" name="title">
        <br><br>

        <h4>본문</h4>
        <textarea name="body" rows="10" cols="40"></textarea>
        <br><br>

        <input type="submit" class="btn btn-dark" value="제출하기">
    </form>
</div>
```

### 2. new 함수 구현 및 url 연결
**views.py**
```python
def new(request):
    return render(request, "new.html")
```

**urls.py**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new', blogapp.views.new, name="new"),
]
```

### new 페이지 결과 화면
<img src="../1st_images/Week_4_4_Test_Image_1.png" width="600" height="auto">

### 3. form태그 action url 연결 및 path 설정
**new.html**
```html
<form action="{% url 'create' %}">
    ...
</form>
```

**urls.py**
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new', blogapp.views.new, name="new"),
    path('blog/create', blogapp.views.create, name="create"),
]
```

### 4. views.py에 create함수 정의
`create`함수는 입력받은 데이터를 `DB`에 저장하는 함수<br/>
`django`의 `utils`의 `timezone`함수 추가<br/>
`django`의 `shortcuts`의 `redirect`함수 추가<br/>
`redirect`함수는 위의 내용을 처리한 후 **인자**로 받은 `url`로 이동

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

...

def create(request):
    blog = Blog()

    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()

    blog.save()

    return redirect('/blog/' + str(blog.id))
```
