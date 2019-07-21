## 5.5주차 - Faker

### 가짜 데이터, 왜 필요한가?
**데이터가 많은 상황**을 염두해 둔 **기능을 구현**할 때<br/>
데이터가 많은 상황을 **재현하기 위해**서 사용

### 설치 명령어
**가상 환경**에 설치
```
$ pip install faker
```

### 사용 방법
```python
from faker import Faker       # Faker 클래스 추가

myfake = Faker()              # Faker 객체 생성

print(myfake.name())          # 가짜 이름 생성
print(myfake.address())       # 가짜 주소 생성
print(myfake.text())          # 가짜 글 생성
print(myfake.state())         # 가짜 주 생성
print(myfake.sentence())      # 가짜 문장 생성
print(myfake.random_number()) # 가짜 난수 생성
```

`Faker`객체 생성시 `ko_KR`을 인자로 넣어주면 한글로<br/>
구성된 가짜 데이터 생성이 가능하나 **몇개의 기능만** 사용 가능

`Faker`객체에 `seed`매서드를 사용하 변하지 않는 데이터 생성 가능
```python
myfake.seed(num)
```
