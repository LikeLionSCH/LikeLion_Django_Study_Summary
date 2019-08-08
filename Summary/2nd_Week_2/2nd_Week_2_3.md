## 2주차 - 3. Serializer 실습 - 코드작성

### 1. 가상환경 생성
```
python -m venv (가상환경 이름)
```

### 2. 필요 패키지 설치
```
pip install djangorestframework
pip install django
```

### 3. Django 프로젝트 생성
```
django-admin startproject (프로젝트 이름)
```
프로젝트 생성후 `cd (프로젝트 이름)`으로 폴더 이동

### 4. Django 앱 생성
```
python manage.py startapp post
```

### 5. settings.py에 앱 추가
**Django Rest Framework**도 등록 해야한다.<br/>
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'post.apps.PostConfig',
]
```

### 6. URL 관리
#### 6-1. 앱 폴더 내부에 urls.py 생성
**계층적**으로 `URL`을 관리하기 위해서 분할한다.<br/>

#### 6-2. 프로젝트 폴더 urls.py에 모듈 추가
```python
from django.contrib import admin
from django.urls import path, include
import post.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(post.urls)),
]
```

### 7. 앱 폴더의 models.py에 모델 클래스 정의
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
```

#### 7-1. 마이그레이션 명령어 실행
```
python manage.py makemigrations
python manage.py migrate
```

### 8. 앱 폴더 내부에 serializer.py 생성 및 작성
어떤 **클래스**의 어떤 **필드**를 사용할 것인지 알려준다.
```python
from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body'] 
        # 모든 필드를 사용할 경우 '__all__' 사용 가능
```

### 8. views.py 작성하기
`rest_framework`의 **viewsets**모듈과 작성한 **모델**과 **Serializer**추가
```python
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer
```

`Django Rest Framework`는 **Claa Base View**다.<br/>
따라서 아래와 같은 **클래스**를 `view`로써 작성한다.<br/>
`viewsets`의 **ModelViewSet**을 상속받는다.<br/>
```python
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### 9. 앱 내부의 urls.py 작성하기
`rest_framework`의 `routers`안에 **DefaultRouter**와<br/>
`include`와 작성한 `views.py`를 추가해준다.
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
```

`rest_framework`는 **Router**를 사용해 `URL`을 결정한다.<br/>
아래와 같이 작성하면 **CRUD**를 기반으로 `URL`을 설정한다.<br/>
```python
router = DefaultRouter()
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
```

### 실행 결과
<img src="../2nd_images/Week_2_3_Test_Image_1.png" width="700" height="auto">
