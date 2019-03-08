### 8주차 - 1. app 재사용 이론

#### App 재사용이란
`App`은 **하나의 역할**만을 담당하도록 설계<br/>
이 `App`중에 다른 웹사이트에서 **공통적**으로 필요한 앱을<br/>
**패키징**해서 다른 웹사이트에서 사용하게 된다.<br/>

**재사용**은 곧 **패키징**을 뜻한다.<br/>

`App`을 묶는 과정, `App`을 설치하는 과정으로 진행<br/>

**패키지**를 **설치**하는 과정은 이미 사용하고 있다.<br/>
```
$ pip install <패키지 이름>
```

#### App을 패키징하는 방법
**필요한 파일**<br/>
1. 패키지 소개 / 사용설명서 / 기능명세서
2. 라이센스
3. 설치하는 방법 과정
4. 파이썬 파일이 아닌 파일 명시

**필요한 파일 이름**<br/>
1. `README.rst`
2. `LICENSE`
3. `setup.py`
4. `MANIFEST.in`

<br/>

### 8주차 - 2. app 재사용 실습

#### 1. 새로운 폴더 생성

#### 2. 재사용할 앱 폴더로 이동

#### 3. 필요한 파일 생성
**README.rst**</br>
앱 기능 명시

**LICENSE**<br/>
코드의 라이센스 명시

**setup.py**<br/>
패키지 설치 과정 명시

**MANIFEST.in**<br/>
파이썬 파일 이외의 파일 명시

#### 4. 패키징 진행
```
$ python setup.py sdist
```

#### 5. 패키징한 앱 설치 및 사용하기
**폴더의 위치**를 잘 파악해 압축된 앱 설치
```
$ pip install dist/login-0.1.tar.gz
```

<br/>

### 8주차 - 3. PostgreSQL 연동 이론, 설치
소규모 프로젝트 단계에서는 `Django`내부에서 지원하는<br/>
`sqlite`로 충분하나 **큰 규모**에서는 외부 `DataBase`사용

#### 데이터베이스
**정보 저장** 공간으로 `Django`와는 별개의 것으로 여러 개가 존재 가능

#### Django에서의 DB
`Django`와는 별개의 것으로 어떤 `DataBase`를<br/>
사용할 것인지는 `settings.py`에 명시

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
**default**로는 `sqlite` 사용<br/>

`settings.py`에 명시한 후 **연결**하는 과정에서는
`migrate`명령어 사용

#### 다른 DataBase 연결하기
1. 다른 `DataBase`설치
2. `settings.py`에 `DataBase`명시
3. `migrate`로 `DataBase`연결

#### PostgreSQL 설치하기
[링크](https://www.postgresql.org/download/)로 이동해 각 운영체제에 맞는 **PostgreSQL** 설치<br/>
**패스워드**와 **포트번호**는 기억하자.

<br/>

### 8주차 - 4. PostgreSQL DB연동 실습

#### 1. pgAdmin 실행 (하나의 서버)

#### 2. postgressSQL 계정 생성
