### 1주차 - 1.기본환경 셋팅

#### 사전작업
1. `git` 설치하기
2. 작업 디렉토리 만들기
3. `python` 설치 확인하기

<br/>

#### VENV 생성 & 가상환경 실행
```
python -m venv myvenv(가상환경명)
```

<br/>

#### 가상환경 실행하기
```
source myvenv/Scripts/activate
source myvenv/bin/activate
```

강의에서는 `Scripts`폴더의 `activate`파일을 실행하라고 하였으나<br/>
본인의 경우에 `Scripts`폴더가 존재하지 않고 `bin`폴더에 `activate`파일 존재<br/>
`source`명령어 대신 `.`을 입력해도 된다,

#### 가상환경 종료하기
```
deactivate
```

<br/>

#### Django 설치하기
> 가상환경을 실행하고 설치

```
pip install django
```

<br/>

### 1주차 - 2.Hello World 이론

#### 유의사항<br/>
오늘 모든 것을 이해하려 하진 말자<br/>
(돌아왔 때 비로소 이해되는 부분들도 있다.)<br/>

<br/>

#### 학습 목표<br/>
`Django`내에서의 **정보**의 흐름<br/>
여기에서 **정보**란 `HTML`파일<br/>

<br/>

#### `Django`는 어떻게 작동할까?<br/>
파일 및 폴더간의 **티키타카**(상호작용)으로 작동<br/>
`Django`를 시작하기 위해선 장고 **프로젝트 생성** 필요<br/>

<br/>

#### `Django`프로젝트 생성 명령어**
```
django-admin startproject <project 이름>
```

<br/>

#### 생성되는 파일 및 폴더 구조<br/>
manage.py<br/>
Project이름으로 된 `폴더`<br/>
├─ `__pycache__`<br/>
├─ `__init__.py`<br/>
├─ `wsig.py`<br/>
├─ `setting.p`y<br/>
└─ `url.py`<br/>
※ `manage.py`파일로 서버를 돌린다.<br/>

<br/>

#### `Django` 서버 작동 명령어
```
python manage.py runserver
```

<br/>

#### App
> 프로젝트의 구성 단위<br/>
> `App`폴더 안의 파일들 간의 티키타카


<br/>

#### App 생성 명령어
```
python manage.py startapp <app이름>
```

<br/>

#### App 폴더 구조
`App` 이름으로 된 폴더<br/>
├─ `migration` 폴더<br/>
├─ `templates` 폴더<br/>
├─ `__init.py`<br/>
├─ `admin.py`<br/>
├─ `apps.py`<br/>
├─ `models.py`<br/>
├─ `test.py`<br/>
└─ `views.py`<br/>

<br/>

#### settings.py
`app` 폴더의 위치와 설정을 저장

<br/>

#### templates 폴더
사용자에게 보여질 화면(html)을 저장

<br/>

#### views.py
사용자에게 보여질 화면(html)이 언제, 어떻게<br/>
처리될지 알려주는 **함수** 작성

<br/>

#### url.py
작성한 html이 어떤 `url**을 입력했을 때<br/>
보여지게할지 설정
