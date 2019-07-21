## 5주차 - 1. 로그인, 회원가입 이론

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

### http Method
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
