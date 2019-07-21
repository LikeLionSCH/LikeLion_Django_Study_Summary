## 4주차 - 5. portfolio (static)

## Django에서 다루는 파일의 종류
1. **Static File (정적 파일)**

**미리** 서버에 **저장**되어 있는 파일<br/>
서버에 저장된 그대로를 서비스해주는 파일<br/>

2. **Dynamic File (동적 파일)**

서버의 데이터들이 어느정도 **가공**된 다음 서비스되는 파일

### Static File (정적 파일)
1. 프로젝트 입장에서 이미 무엇인지 아는 파일
    + 개발할 때 미리 준비해둔 파일 = "**static**"
2. 웹 서비스 이용자들이 업로드하는 파일
    + "**media**"

### Static File의 처리 과정
1. **Static 파일**의 **위치 찾기**
2. **Static 파일**을 한 곳에 **모으기**

우리가 해야할 것<br/>
1. **Static 파일**들을 담을 폴더 만들기
    + (**App폴더 내부**에) **Static** 폴더 생성 및 파일 저장
2. **Static 파일**의 위치 알려주기
    + `settings.py`에서 알려주기
3. **Static 파일**을 모으기
    + `$ python manage.py collectstatic` (명령어)

### 1. portfolio.html 생성 및 기본 연결
1. `portfolio`앱 생성
```
$ python manage.py startapp portfolio
```
2. `settings.py`에 App 추가
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
]
```
3. `templates`폴더 생성 및 `portfolio.html`생성
4. `views.py`에 `portfolio`함수 정의
```python
def portfolio(request):
    return render(request, "portfolio.html")
```
3. `portfolio`의 `views.py` import 및 `urls.py`에 `path`추가
```python
import portfolio.views
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new', blogapp.views.new, name="new"),
    path('blog/create', blogapp.views.create, name="create"),
    path('portfolio', portfolio.views.portfolio, name="portfolio"),
]
```

4. Portfolio 관련된 `a`태그에 **템플릿 태그**로 `url` 생성
```html
<a class="dropdown-item" href="{% url 'portfolio' %}">Portfolio</a>
```

### 2. portfolio앱에 static폴더 생성 및 파일 추가<br/>
<img src="../1st_images/Week_4_5_Test_Image_1.png" width="400" height="auto">

### 3. settings.py에 static폴더 경로 추가
`STATICFILES_DIRS`은 `static`파일이 **어디 있는지** 알려주는 변수<br/>
`STATIC_ROOT`은 `static`파일들이 **어디로 모일 것**인지 알려주는 변수
```python
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'portfolio', 'static')
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

### 4. static 파일들을 모으는 명령어 사용
```
$ python manage.py collectstatic
```

최상위 폴더에 `static`폴더가 생성<br/>
<img src="../1st_images/Week_4_5_Test_Image_2.png" width="200" height="auto">

### 5. portfolio.html에서 static파일 사용
`portfolio.html` 최상단에 아래 코드 추가
```
{% load staticfiles %}
```

`img`태그에 이미지 경로 추가
```html
<a href="#"><img class="card-img-top" src="{% static 'first_logo.png' %}" alt=""></a>
```

**결과 화면**<br/>
<img src="../1st_images/Week_4_5_Test_Image_3.png" width="600" height="auto">
