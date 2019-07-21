## 2주차 - 2.wordcount 실습 part 1

### 1. 가상 환경을 켜고 시작
```
source myvenv/bin/activate
```

### 2. Djnago 프로젝트 생성
```
django-admin startproject <project 이름>
```

### 3. 프로젝트 경로 이동
```
cd <project 이름>
```

### 4. App 생성
```
python manage.py startapp wordcount
```

### 5. settings.py 에 App 추가
`INSTALLED_APPS`리스트에 `wordcount`앱 추가
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wordcount.apps.WordcountConfig',
]
```

### 6. 템플릿 폴더 생성 및 템플릿 생성
`wordcount`앱 안에 `templates`폴더 생성<br/>
`templates`폴더 안에 `home.html`, `about.html`, `result.html` 생성

### 7. views.py 에 함수 정의
`render(request, 템플릿 이름, 사전형 객체)`

`home`함수 정의
```python
def home(request):
    return render(request, 'home.html')
```

`about`함수 정의
```python
def about(request):
    return render(request, 'about.html')
```

### 8. url 설계
1. `wordcount`앱에 `views.py` import
2. `urlpatterns`리스트에 `path`추가

```python
from django.contrib import admin
from django.urls import path
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wordcount.views.home, name="home"),
    path('about/', wordcount.views.about, name='about'),
]
```

### 9. 페이지 연결
**템플릿 태그** 사용<br/>

`home.html`에 `about.html`연결
```
<a href="{% url 'about' %}">About</a>
```

`about.html`에 `home.html`연결
```
<a href="{% url 'home' %}">About</a>
```
