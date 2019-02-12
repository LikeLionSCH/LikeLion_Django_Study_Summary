### 5주차 - 1. 로그인, 회원가입 이론
`Django`에서 제공하는 **함수** 이용

### 회원가입 로그인 로그아웃
1. 계정을 관리하는 **앱** 생성
2. 앱에서 회원가입, 로그인, 로그아웃 **함수** 구현
3. 페이지에 해당하는 `url`, `templates` 구현

추가할 모듈
```python
from django.contrib.auth.models import User
from django.contrib import auth
```

회원가입 함수
- `User.objects.create_user(username, password)`

로그인 함수
- `auth.authenticate()` : 등록된 회원인지 확인
- `auth.login(request, user)` : 로그인

로그아웃 함수
- `auth.logout(request)` : 로그아웃

#### http Method
`http`상에 정보를 주고받는 방식<br/>
```html
<form action="{% url 'thisisurl' %}">
...
</form>
```
`method`를 지정하지 않으면 **GET** 방식<br/>
그래서 `request.GET[]`로 `form`의 입력값 저장<br/>
**GET** 방식으 주고받은 데이터는 `url`에 노출<br/>
`url`로 직접 정보 노출되지 않는 **POST** 방식 사용

| 상황        | method |
| ----------- | ------ |
| 데이터 조회 | GET    |
| 데이터 생성 | POST   |
| 데이터 수정 | PUT    |
| 데이터 삭제 | DELETE |

<br/>

### 5주차 - 2. 로그인, 회원가입 실습
#### 1. 계정을 관리 할 앱 생성
#### 2. `settings.py`에 앱 추가

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

#### 3. 앱에 로그인, 회원가입 템플릿 추가
`base.html`에 템플릿 태그로 `url`생성
```html
<li class="nav-item">
    <a class="nav-link" href="{% url 'signup' %}">Sign up</a>
</li>
<li class="nav-item">
    <a class="nav-link" href="{% url 'login' %}">Login</a>
</li>
```

#### 4. 계정 관리 앱 `url`설정

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

#### 5. 회원가입, 로그인 페이지 form 태그 작성
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


#### 6. 계정 관리 앱의 `views.py`작성
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

#### 7. 로그아웃 기능 구현
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

<br/>

### 5주차 - 3. Pagination 이론
**대규모 데이터**를 다루는 웹서비스에서 **필수**적인 기능<br/>
`home.html`과 `views.py`를 수정하여 구현

#### views.py
`Django`에서 기본적으로 지원하는 기능 사용

추가할 모듈
```python
from django.core.paginator import Paginator
```

1. **무슨** 객체를, 한 페이지 당 **몇 개**씩 Pagination할 지 결정
```python
Paginator(어떤 객체를, 한페이지당 몇 개 씩)
```

2. 자른 페이지를 **한 단위**로 가지고 사용하여 가져오기
```python
페이지네이터객체.get_page(페이지번호)
```

3. 원하는 페이지를 `html`에 띄우기<br/>
페이지 객체의 메소드함수 + template 언어

#### Paginator Class Vs Page Class
| Paginator Object        | Page Object         |
| ----------------------- | ------------------- |
| 잘려진 식빵 조각 뭉텅이 | 잘려진 식빵 한 조각 |

최종 목적 : Page Object

#### Page 객체의 메소드 함수
주로 사용하는 메소드 함수

| 함수                       | 뜻                                      |
| -------------------------- | --------------------------------------- |
| page.count()               | 총 객체 수 반환                         |
| page.num_pages()           | 총 페이지 개수 반환                     |
| page.page(n)               | n번째 페이지 반환                       |
| page.page_range()          | (1부터 시작)페이지 리스트 반환          |
| page.get_page(n)           | n번째 페이지 가져오기                   |
| page.has_next()            | 다음 페이지가 있으면 True, 없으면 False |
| page.has_previous()        | 이전 페이지가 있으면 True, 없으면 False |
| page.previous_page_numer() | 이전 페이지 번호 반환                   |

#### 원하는 페이지 번호를 얻는 방법
아래와 같은 코드를 사용
```python
page = request.GET.get('page')
```
`request.GET`은 **딕셔너리** 자료형<br/>
`.get` : **딕셔너리 자료형**에 **key**값을 인자로 주면 **value**반환

아래와 같은 URL의 경우<br/>
`www.google.com?thisIsAGetVarKey=3&ThisIsAnotherOne=hello`<br/>
`request.GET`은 `{"thisIsAGetVarKey":3, "ThisIsAnotherOne":hello}`

**Pagination**의 `url`이 `127.0.0.1:8000/?page=2`일 경우<br/>
`request.GET`은 `{"page":2}`로 **key**값은 `page`, **value**는 `2`<br/>

따라서 `page = request.GET.get('page')`는 `request.GET`중에서<br/>
`page`를 **key**값으로 하는 **value(페이지번호)**를 반환해 `page`변수에 담으라는 뜻<br/>
결국 `page`변수 안에는 `request`를 보낸 **페이지 번호**가 **저장**된다.<br/>
`get_page`함수를 사용해 페이지를 실제로 가져와 띄워주면 된다.

<br/>

### 5주차 - 4. Pagination 실습
