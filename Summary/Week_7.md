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
```
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

<a href="{% provider_login_url 'google' %}">Google Login</a>
```

<br/>

### 7주차 - 3. API 이론

#### API란 무엇인가?
**A**pplicaion **P**rogramming **I**nterface 의 약자<br/>
**응용프로그램**에서 사용할 수 있도록,<br/>
**운영체제**나 프로그래밍 **언어**가 제공하는 기능을<br/>
**제어**할 수 있는 **인터페이스**를 뜻한다.<br/>

가지고 있지 않은, 사용하고 싶은 **외부기능**을 사용하도록 **연결**

#### 지도 API
1. 경로 찾기
2. 위치 검색
3. etc...

오늘의 학습 목표 = **특정 지점**의 위치 표시

<br/>

### 7주차 - 4. API 실습

#### 1. [네이버 클라우드 플랫폼](https://www.ncloud.com) 회원가입

#### 2. 네이버 Maps API 이용 신청 하기

#### 3. 어플리케이션 등록 (Web Dynamic Map 사용)

#### 4. 인증 정보 확인 및 저장

#### 5. 예시 코드 사용해보기
`Client_id`에는 인증 정보에 있는 값 사용<br/>

**지도 띄워보기**
```html
...

<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
    <title>간단한 지도 표시하기</title>
    <script type="text/javascript" src="https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId=Client_id"></script>
</head>

<body>

    ...

    <div id="map" style="width:50%;height:400px;"></div>

    <script>
        var mapOptions = {
            center: new naver.maps.LatLng(37.3595704, 127.105399),
            zoom: 12
        };

        var map = new naver.maps.Map('map', mapOptions);
    </script>
</body>

</html>
```

**마커 및 위치 정보 띄워보기**
```html
...

<!DOCTYPE html>
<html>

<head>
    ...
</head>

<body>

    ...

    <div id="map" style="width:50%;height:400px;"></div>

    <script>
    var HOME_PATH = window.HOME_PATH || '.';

    var cityhall = new naver.maps.LatLng(37.5666805, 126.9784147),
        map = new naver.maps.Map('map', {
            center: cityhall.destinationPoint(0, 500),
            zoom: 10
        }),
        marker = new naver.maps.Marker({
            map: map,
            position: cityhall
        });

    var contentString = [
        '<div class="iw_inner">',
        '   <h3>서울특별시청</h3>',
        '   <p>서울특별시 중구 태평로1가 31 | 서울특별시 중구 세종대로 110 서울특별시청<br />',
        '       <img src="' + HOME_PATH + '/img/example/hi-seoul.jpg" width="55" height="55" alt="서울시청" class="thumb" /><br />',
        '       02-120 | 공공,사회기관 &gt; 특별,광역시청<br />',
        '       <a href="http://www.seoul.go.kr" target="_blank">www.seoul.go.kr/</a>',
        '   </p>',
        '</div>'
    ].join('');

    var infowindow = new naver.maps.InfoWindow({
        content: contentString
    });

    naver.maps.Event.addListener(marker, "click", function(e) {
        if (infowindow.getMap()) {
            infowindow.close();
        } else {
            infowindow.open(map, marker);
        }
    });

    infowindow.open(map, marker);
    </script>
</body>

</html>
```

<br/>

### 7.5주차 - 썸네일 만들기

#### Thumbnail
이미지 파일을 **대표**하는 이미지

#### 기능 장점
1. Thumbnail 파일 지정 용이
2. 파일 용량 관리 용이
3. 파일 분류에 효율적

#### 실습
1. 기본적인 **Media 파일** 사용 설정
    + `models.py`에 `model`정의
    + `settings.py`에 경로 설정
    + `urls.py`에 `path` 추가
    + `admin.py`에 `model`등록
    + **migrate** 진행
    + `views.py`의 함수 이미지를 사용하도록 수정
    + `html`에 전달 받은 이미지 출력
2. pip **패키지** 설치

```
$ pip install pillow django-imagekit
```
3. settings.py에 앱 추가

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    ...

    # Imagekit
    'imagekit'
]
```
4. models.py에 model 수정

필요한 모듈 추가<br/>
`imagekit.models`의 `ImageSpecField`함수 이용<br/>
`source`인자는 **이미지 주소**, 이미지 **크기를 조정**하기 위하여<br/>
`processors`인자에 `list`형식으로 `ResizeToFill`함수 사용
```python
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Pictures(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to="blog_img")
    image_thumbnail = ImageSpecField(
        source="image", processors=[ResizeToFill(120, 60)]
    )

```

5. html에 Thumbnail 띄우기

기존의 이미지를 띄우는 것과 동일<br/>
이미지를 띄울땐 뒤에 **꼭** `.url`을 붙여야한다.
```html
<img src="{{ blog.image_thumbnail.url }}">
```

#### ImageSpecField함수 속성
확장자 지정
```python
thumbnail = ImageSpecField(..., format='JPEG')
```

압축 방식 지정
```python
thumbnail = ImageSpecField(..., options={
    'quality': 60,
})
```

...etc
