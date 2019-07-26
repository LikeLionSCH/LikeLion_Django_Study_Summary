## 1주차 - 3. CBV (2)

### 1. 프로젝트 생성
```
django-admin startproject CBV
```

### 2. 앱 생성
```
python manage.py createapp classBaseCrud
```

### 3. settings.py에 앱 추가
`settings.py`의 `INSTALLED_APPS`리스트 수정
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'classBaseCrud.apps.ClassBaseCrudConfig',
]
```

### 4. 앱 내부에 urls.py생성 및 작성
작성할 **클래스**에 맞는 `url path`작성<br/>
함수를 기반으로 작성했을 때와 많은 차이는 존재하지 않는다.<br/>
`.as_view()`는 `views.py`에 작성한 클래스 안의 **매소드**에 해당한다.<br/>
```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogView.as_view(), name="list"),
    path("create/", views.BlogCreate.as_view(), name="create"),
    path("read/<int:pk>", views.BlogRead.as_view(), name="read"),
    path("update/<int:pk>", views.BlogUpdate.as_view(), name="update"),
    path("delete/<int:pk>", views.BlogDelete.as_view(), name="delete"),
]
```

### 5. 프로젝트의 urls.py에 앱 urls.py추가
`django.urls`의 `include`모듈을 추가<br/>
앱의 `urls.py`파일을 프로젝트 `urls.py`에 추가
```python
from django.contrib import admin
from django.urls import path, include
import classBaseCrud.urls
import classBaseCrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', include(classBaseCrud.urls)),
]
```

### 6. models.py 작성하기
제목, 생성일, 수정일, 본문을 갖는 아래와 같은 `ClassBlog`클래스 작성<br/>
```python
class ClassBlog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    
    def __str__(self):
        return self.title
```

### 7. admin.py에 model등록
```python
from django.contrib import admin
from .models import ClassBlog

admin.site.register(ClassBlog)
```

### 8. views.py 작성하기

#### 1) 필요한 모듈 추가
게시글 목록을 보여주는 `ListView`<br/>
새로운 게시글을 생성하는 `CreateView`<br/>
게시글의 상세 내용을 보여주는 `DetailView`<br/>
게시글을 수정하는 `UpdateView`<br/>
게시글을 삭제하는 `DeleteView`<br/>
```python
from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import ClassBlog
```

#### 2) 모듈을 상속해 클래스 작성
각 기능에 맞는 모듈을 **상속**해 클래스 객체 작성<br/>
작업이 성공적으로 완료되었을 경우 이동하는 `URL`을 설정하기 위해<br/>
`reverse_lazy()`함수 사용 인자로는 **URL 이름**을 넣어주면 된다.<br/>
`get_absolute_url()`, `reverse()`와 같은 함수도 있다.<br/>
```python
class BlogView(ListView):
    model = ClassBlog


class BlogCreate(CreateView):
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy('list')


class BlogRead(DetailView):
    model = ClassBlog
    

class BlogUpdate(UpdateView):
    model = ClassBlog
    fields = ["title", "body"]
    success_url = reverse_lazy("list")


class BlogDelete(DeleteView):
    mdoel = ClassBlog
    success_url = reverse_lazy("list")
```
