## 4.5주차 - 템플릿 상속, url 관리

### 템플릿 상속
코드 **재사용**<br/>
**일관된** UI 구성 및 **변경** 용이

### 템플릿 상속의 구현
1. 프로젝트 폴더에 `templates`폴더 생성
2. `templates`폴더에 `base.html`생성

<img src="../1st_images/Week_4_6_Test_Image_1.png" width="200" height="auto">

3. `base.html`에 **중복되는** 코드 작성<br/>

```html
<head>
    중복되는 내용...
</head>

<body>
    중복되는 내용...

    {% block contents %}
    {% endblock %}
</body>
```

4. `settings.py`에 `base.html`위치 작성

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['blogproject/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
5. 겹치는 내용 삭제 후 `base.html` 사용

```html
{% extends 'base.html' %}

{% block contents %}
<body>
    중복되지 않는 내용...
</body>
{% endblock %}
```

### url의 효율적 관리
1. 관리할 앱 폴더 내부에 `urls.py`생성
2. `urls.py`에 `path` 작성

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name="search"),
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
]
```

3. 기존의 `urls.py`와 앱의 `urls.py` 연결

`django.urls`의 `include`모듈 추가<br/>
`path('blog/', include('blogapp.urls'))`추가<br/>
`blogapp`의 `urls.py`를 `include` 모듈을 사용해<br/>
하나의 앱에 **동일한** `blog/` 패턴의 `path` 추가
```python
from django.urls import path, include

...

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio', portfolio.views.portfolio, name="portfolio"),
]
```
