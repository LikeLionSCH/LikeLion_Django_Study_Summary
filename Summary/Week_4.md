### 4주차 - 1. pk, path converter, get_object_or_404

#### 해야할 것
1. 글자 수 제한 (글자 **상한선 제시**)
2. ...more 라는 글자에 **링크 달기**
3. 링크를 클릭했을 때 `detail.html` 페이지 내보내기

#### 1. models.py에 함수 정의 하기
본문의 내용을 **100글자**로 **제한**하는 함수 정의<br/>
자신 `object`의 `body`를 **100글자**까지 반환
```python
def summary(self):
    return self.body[:100]
```

#### 2. home.html의 본문 내용 출력 변경
`blog` 객체의 `summary`함수 사용
```html
{% for blog in blogs.all %}
    <h1> {{ blog.title }} </h1>
    <h3> 날짜 </h3>
    <p> {{ blog.pub_date }} </p>

    <h3> 본문 미리보기 </h3>
    <p> {{ blog.summary }} </p>
    <br/>
    <br/>
{% endfor %}
```

#### 3. 세부 내용 표시 링크 추가
`a`태그 사용
```html
{% for blog in blogs.all %}
    <h1> {{ blog.title }} </h1>
    <h3> 날짜 </h3>
    <p> {{ blog.pub_date }} </p>

    <h3> 본문 미리보기 </h3>
    <p>
        {{ blog.summary }}
        <a href="#"> ...more </a>
    </p>
    <br/>
    <br/>
{% endfor %}
```

#### 4. 링크를 클릭했을 때 detail 페이지 내보내기
**문제점**<br/>
블로그 `object`가 매우 많아 졌을 때<br/>
어떻게 `detail.html`파일을 **생성**하고 **출력**할 것인가?

**해결법**<br/>
`detail.html`은 하나만 생성<br/>
**특정 번호**의 블로그 **객체** 내용 요청시 해당 **객체**를 출력<br/>
**url pattern = 사이트이름/blog/객체번호**<br/>
해당 번호의 **객체가 없다면** `404 ERROR` 출력<br/>

**알아야 하는 것**
1. 블로그 객체 번호 (**PK**)
2. url pattern 디자인 및 연결 (**Path Converter**)
3. 블로그 객체 미 존재 시 404 띄우기 (**Get Object or 404**)


##### 1. url 패턴 디자인하기
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>', blog.views.detail, name="detail"),
]
```
`<int:blog_id>`이 부분이 **Path Converter**<br/>
**계층적 `url` 디자인**에 있어서 핵심 부분<br/>
`사이트이름/blog/정수`형태로 `url`을 설계<br/>
`blog_id`는 `views.py`의 함수에 전달해 주는 **인자**<br/>

**`detail.html`을 출력하는 함수의 정의**
```python
def detail(request, blog_id):
    pass
```

**`home`함수와 비교**
```python
def home(request):
    blogs = Blog.objects

    return render(request,
                  'home.html',
                  {'blogs': blogs})
```
`home`함수는 `request`만 들어오면 실행되는 함수<br/>
`request`이외의 정보는 **필요가 없기** 때문에 인자가 `request` 하나다.<br/>
하지만 `detail`함수는 `request`외에 추가 정보 필요하다.<br/>
**몇 번째 객체**를 출력할 것인지에 대한 정보 필요 따라서 **인자**에 `blog_id`추가

**Path Converter**<br/>
**여러 객체**들을 다루는, **계층적인 `url`**을 자동 생성할 때 유리<br/>
`<type : 변수이름>`<br/>
타입은 `int`, `str`, `uuid` 등....

##### 2. views.py에 detail함수 작성하기
**특정 번호의 객체**를 가져와 사용해야 하기 때문에<br/>
`home`함수와 같이 `objects`메서드 사용을 하면 안된다.<br/>
따라서 `get_object_or_404(클래스, 검색 조건)`매서드를 사용<br/>

**views.py에 get_object_or_404 모듈 추가**
```python
from django.shortcuts import render, get_object_or_404
```

`pk(primary key)` : 객체들의 이름표, 구분자, 데이터의 대표값

**blog_id를 pk로 사용하여** `get_object_or_404` **함수 사용**
```python
def detail(request, blog_id):
    blog_detail = Blog.get_object_or_404(Blog, pk=blog_id)

    return render(request,
                  'detail.html',
                  {'blog': blog_detail})
```
