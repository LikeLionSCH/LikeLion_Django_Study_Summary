## 8주차 - 3. PostgreSQL 연동 이론, 설치
소규모 프로젝트 단계에서는 `Django`내부에서 지원하는<br/>
`sqlite`로 충분하나 **큰 규모**에서는 외부 `DataBase`사용

### 데이터베이스
**정보 저장** 공간으로 `Django`와는 별개의 것으로 여러 개가 존재 가능

### Django에서의 DB
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

### 다른 DataBase 연결하기
1. 다른 `DataBase`설치
2. `settings.py`에 `DataBase`명시
3. `migrate`로 `DataBase`연결

### PostgreSQL 설치하기
[링크](https://www.postgresql.org/download/)로 이동해 각 운영체제에 맞는 **PostgreSQL** 설치<br/>
**패스워드**와 **포트번호**는 기억하자.
