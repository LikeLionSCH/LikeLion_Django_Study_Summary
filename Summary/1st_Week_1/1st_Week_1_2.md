## 1주차 - 2.Hello World 이론

### 유의사항<br/>
오늘 모든 것을 이해하려 하진 말자<br/>
(돌아왔 때 비로소 이해되는 부분들도 있다.)<br/>

### 학습 목표<br/>
`Django`내에서의 **정보**의 흐름<br/>
여기에서 **정보**란 `HTML`파일<br/>

### `Django`는 어떻게 작동할까?<br/>
파일 및 폴더간의 **티키타카**(상호작용)으로 작동<br/>
`Django`를 시작하기 위해선 장고 **프로젝트 생성** 필요<br/>

### `Django`프로젝트 생성 명령어
```
django-admin startproject <project 이름>
```

### 생성되는 파일 및 폴더 구조<br/>
manage.py<br/>
Project이름으로 된 `폴더`<br/>
├─ `__pycache__`<br/>
├─ `__init__.py`<br/>
├─ `wsig.py`<br/>
├─ `setting.py`<br/>
└─ `url.py`<br/>
※ `manage.py`파일로 서버를 돌린다.<br/>

### `Django` 서버 작동 명령어
```
python manage.py runserver
```

### App
프로젝트의 구성 단위<br/>
`App`폴더 안의 파일들 간의 티키타카

### App 생성 명령어
```
python manage.py startapp <app이름>
```

### App 폴더 구조
`App` 이름으로 된 폴더<br/>
├─ `migration` 폴더<br/>
├─ `templates` 폴더<br/>
├─ `__init.py`<br/>
├─ `admin.py`<br/>
├─ `apps.py`<br/>
├─ `models.py`<br/>
├─ `test.py`<br/>
└─ `views.py`<br/>

### 지금 알아둬야 할 폴더와 파일 역할
**settings.py**<br/>
`app` 폴더의 위치와 설정을 저장

**templates 폴더**<br/>
사용자에게 보여질 화면(html)을 저장

**views.py**<br/>
사용자에게 보여질 화면(html)이 언제, 어떻게<br/>
처리될지 알려주는 **함수** 작성

**url.py**<br/>
작성한 html이 어떤 `url`을 입력했을 때<br/>
보여지게할지 설정
