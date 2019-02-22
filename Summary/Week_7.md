### 7주차 - 1. 소셜 로그인 이론

#### 배우는 주제 자체가 수업 목표

#### Social 계정으로 로그인
`pip` 패키지 `allauth` 사용

|         | 기존의 방식                            | Social 계정 방식                             |
| ------- | -------------------------------------- | -------------------------------------------- |
| DB      | DB와 DB를 다루는 로직이 한 공간에 존재 | DB와 DB를 다루는 로직이 다른 공간에 존재     |
| Request | request 요청시 바로 실행               | SNS 서버와 request와 token을 주고받으며 실행 |

<br/>

### 7주차 - 2. 소셜 로그인 실습

#### 1. pip 패키지 설치
```
$ pip install django-allauth
```

#### 2. settings.py 설정
`INSTALLED_APPS`**리스트**에 내용 추가<br/>
`django.contrib.sites`와 `allauth`, `provider`설정 추가
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp.apps.BlogappConfig',
    'portfolio.apps.PortfolioConfig',
    'accounts.apps.AccountsConfig',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # provider
    'allauth.socialaccount.providers.google',
]
```

로그인시 **redirect**되는 `url`**변수**인 `LOGIN_REDIRECT_URL`**변수**와<br/>
`AUTHENTICATION_BACKENDS`**튜플**과 `SITE_ID`**변수** 생성
```python
LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of 'allauth'
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth' specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1
```

#### 3. url 설정
`allauth`패키지 내부에 이미 정의<br/>
`include`모듈을 사용해 `allauth.urls`추가
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('sociallogin/', include('allauth.urls')),
    path('portfolio', portfolio.views.portfolio, name="portfolio"),
]
```

#### 4. migrate 진행
```python
$ python manage.py migrate
```

#### 5. admin 페이지의 site설정 변경
`Domain name`과 `Display name`을 사용할 주소로 변경<br/>
해당 실습에서는 **로컬**에서 작업하므로 `127.0.0.1:8000`사용

#### 6. admin 페이지에서 social application 등록
[링크](https://console.developers.google.com)에서 `Client id`와 `Secret key`확인 후 등록

#### 7. html위에 띄워주기
```html
{% load socialaccount %}
{% providers_media_js %}

...

<a href="/sociallogin/signup">Google Sign Up</a> /
<a href="{% provider_login_url 'google' %}">Google Login</a>
```
