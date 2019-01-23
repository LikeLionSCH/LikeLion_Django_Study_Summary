### 3주차 - 1.model&admin 이론

#### 학습목표
`Model`에 데이터를 **어떻게** 담을 것 인가?<br/>
`Model`의 데이터를 **어떻게** `View`로 넘길 것인가?<br/>
데이터를 **어떻게** 화면에 띄울 것인가?

#### 선행지식
**Python - Class**

#### 데이터베이스를 다루는 Model
처리할 데이터의 형식을 `model.py`에 `class`로 정의<br/>

- `model.py` : 데이터를 만드는 공장
- `class` : 데이터 처리 방법

`model.py`에 `class`만 정의한다고 끝난 것이 아니다.<br/>
`DataBase` = 정보 저장 공간, `DataBase`는 장고와 별개<br/>
`Django`의 `model`안에 정의한 `class`를 `DataBase`에 알려줘야 한다.

**사용되는 명령어**

`DataBase`가 알도록 하는 과정
```
$ python manage.py makemigrations
```

`DataBase`에 적용하는 과정
```
$ python manage.py migrate
```

#### 127.0.0.1/admin
`admin`계정 생성 명령어
```
$ python manage.py createsuperuser
```
`admin.py`에 들어가 데이터 등록

#### 한 줄 요약
`DataBase`에 **어떻게** 생긴 데이터를 넣을지 **정의**하고,<br/>
거기에 `admin`권한으로 **데이터**를 **저장**(= 글 쓰기)
