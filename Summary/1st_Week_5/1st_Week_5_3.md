## 5주차 - 3. Pagination 이론

**대규모 데이터**를 다루는 웹서비스에서 **필수**적인 기능<br/>
`home.html`과 `views.py`를 수정하여 구현

### views.py
`Django`에서 기본적으로 지원하는 기능 사용

추가할 모듈
```python
from django.core.paginator import Paginator
```

1. **무슨** 객체를, 한 페이지 당 **몇 개**씩 Pagination할 지 결정
```python
Paginator(어떤 객체를, 한페이지당 몇 개 씩)
```

2. 자른 페이지를 **한 단위**로 가지고 사용하여 가져오기
```python
페이지네이터객체.get_page(페이지번호)
```

3. 원하는 페이지를 `html`에 띄우기<br/>
페이지 객체의 메소드함수 + template 언어

### Paginator Class Vs Page Class
| Paginator Object        | Page Object         |
| ----------------------- | ------------------- |
| 잘려진 식빵 조각 뭉텅이 | 잘려진 식빵 한 조각 |

최종 목적 : Page Object

### Page 객체의 메소드 함수
주로 사용하는 메소드 함수

| 함수                        | 뜻                                      |
| --------------------------- | --------------------------------------- |
| page.count()                | 총 객체 수 반환                         |
| page.num_pages()            | 총 페이지 개수 반환                     |
| page.page(n)                | n번째 페이지 반환                       |
| page.page_range()           | (1부터 시작)페이지 리스트 반환          |
| page.get_page(n)            | n번째 페이지 가져오기                   |
| page.has_next()             | 다음 페이지가 있으면 True, 없으면 False |
| page.has_previous()         | 이전 페이지가 있으면 True, 없으면 False |
| page.previous_page_number() | 이전 페이지 번호 반환                   |

### 원하는 페이지 번호를 얻는 방법
아래와 같은 코드를 사용
```python
page = request.GET.get('page')
```
`request.GET`은 **딕셔너리** 자료형<br/>
`.get` : **딕셔너리 자료형**에 **key**값을 인자로 주면 **value**반환

아래와 같은 URL의 경우<br/>
`www.google.com?thisIsAGetVarKey=3&ThisIsAnotherOne=hello`<br/>
`request.GET`은 `{"thisIsAGetVarKey":3, "ThisIsAnotherOne":hello}`

**Pagination**의 `url`이 `127.0.0.1:8000/?page=2`일 경우<br/>
`request.GET`은 `{"page":2}`로 **key**값은 `page`, **value**는 `2`<br/>

따라서 `page = request.GET.get('page')`는 `request.GET`중에서<br/>
`page`를 **key**값으로 하는 **value(페이지번호)**를 반환해 `page`변수에 담으라는 뜻<br/>
결국 `page`변수 안에는 `request`를 보낸 **페이지 번호**가 **저장**된다.<br/>
`get_page`함수를 사용해 페이지를 실제로 가져와 띄워주면 된다.
