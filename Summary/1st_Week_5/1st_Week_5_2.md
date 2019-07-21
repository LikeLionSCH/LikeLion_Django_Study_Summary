## 5주차 - 2. 로그인, 회원가입 실습

### 1. 계정을 관리 할 앱 생성

### 2. `settings.py`에 앱 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogapp.apps.BlogappConfig',
    'portfolio.apps.PortfolioConfig',
    'accounts.apps.AccountsConfig',
]
```

### 3. 앱에 로그인, 회원가입 템플릿 추가
`base.html`에 템플릿 태그로 `url`생성
```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'signup' %}">Sign up</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{% url 'login' %}">Login</a>
</li>
```

### 4. 계정 관리 앱 `url`설정

`accounts`앱의 `urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
]
```

프로젝트 폴더의 `urls.py`의 `urlpatterns`리스트
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio', portfolio.views.portfolio, name="portfolio"),
]
```

### 5. 회원가입, 로그인 페이지 form 태그 작성
**POST**방식 사용<br/>
**csrf_token**은 보안을 위해 사용

**signup.html**
```html
<form action="{% url 'signup' %}" method="POST">
    {% csrf_token %}
    ...
</form>
```

**login.html**
```html
<form action="{% url 'login' %}" method="POST">
    {% csrf_token %}
    ...
</form>
```


### 6. 계정 관리 앱의 `views.py`작성
`User` 모듈과 `auth` 모듈 추가<br/>
```python
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
```

**login함수 설명**<br/>
`request`방식이 **POST**이면 `input`태그의 입력값으로<br/>
`username`, `password` 변수 값 저장 후 `authenticate`함수 호출로<br/>
**존재하는 계정**일 경우 저장 된 **변수의 값**이 `None`이 아니므로<br/>
`login`함수 호출 후 `redirect`함수 호출로 `home.html`로 이동<br/>
**존재 하지 않는 계정**인 경우 **변수의 값**이 `None`이므로 에러메세지와 함께<br/>
`login`페이지 렌더링 `request`방식이 **POST**가 아닐경우 `login`페이지 렌더링

```python
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(
            request, username=username, password=password
        )

        if user is not None:
            auth.login(request, user)

            return redirect('home')

        else:
            return render(request, "login.html", {
                'error': 'Username or Password is incorrect.',
            })

    else:
        return render(request, "login.html")
```

**signup함수 설명**<br/>
`request`방식이 **POST**이고 입력 비밀번호와 확인 비밀번호가 **같으면**<br/>
`input`태그의 입력값으로 `create_user`함수 호출로 `User`객체 생성<br/>
`login`함수 호출로 계정이 생성되면 **자동으로 로그인** 되도록 한 후<br/>
`redirect`함수 호출로 `home.html`로 이동 실패시 회원가입 페이지 랜더링

```python
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            auth.login(request, user)

            return redirect('home')

    return render(request, "signup.html")
```

### 7. 로그아웃 기능 구현
`urls.py`에 `path`추가
```python
urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
```

`auth`의 `logout`함수 사용

```python
def logout(request):
    if request.method == "POST":
        auth.logout(request)

        return redirect("home")

    return render(request, "login.html")
```
