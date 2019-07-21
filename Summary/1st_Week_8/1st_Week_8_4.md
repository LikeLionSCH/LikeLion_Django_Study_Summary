## 8주차 - 4. PostgreSQL DB연동 실습

### 1. pgAdmin 실행 (하나의 서버)

### 2. postgreSQL 로그인

### 3. DataBase 생성

### 4. Django 프로젝트와 연동
`settings.py`의 `DATABASES`딕셔너리 수정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'postgres',
        'PASSWORD': '내 비밀번호',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### 5. migrate 명령어 실행
```
$python manage.py migrate
```

### 6. admin 계정 새로 생성하기
기존의 `admin`계정 또한 `sqlite`에 포함되기 때문이다.
```
$python manage.py createsuperuser
```
