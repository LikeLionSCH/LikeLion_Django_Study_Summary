### 6주차 - 1. form 이론

#### Form(입력공간)
**Model**형식에 맞는 **Form**만들기<br/>
`html`로 만드는 것은 **한계**가 존재

#### forms.py
`html`의 `<form>`태그와 매칭<br/>

**Model**을 기반으로한 입력공간 만들기<br/>
```python
from django import forms.ModelForm
```

클래스 정의 방법<br/>
```python
from django import forms

class myForm(forms.ModelForm):
    class Meta:
        # 어떤 모델 기반으로한 입력공간인지
        # 그 모델 중에서 어떤 항목을 입력받을지

    img = forms.ImageField     # 사진
    text = forms.TextField     # 글 (forms.CharField)
    time = forms.DateTimeField # 시간 등등
```

`views.py`에 끌어다 사용하기<br/>
```python
from .form import myForm

'''
create함수
1. 처음 new.html에 들어가면 빈 입력공간 띄우기 (GET)
2. 이용자가 데이터 입력한 값 처리하기 (POST)
'''
def create(request):
    # request가 POST일 경우
    if request.method == 'POST':
        # 이용자가 데이터 입력한 값 처리하기 (POST)

    # request가 GET일 경우
    else:
        # 처음 new.html에 들어가면 빈 입력공간 띄우기 (GET)
```

사용자에게 값을 입력받지 않고 사용하고 싶을 경우<br/>

`is_valid()` : 입력값이 잘 입력되었는지 검사하는 메소드
```python
from .form import myForm

# 날짜 정보는 사용자에게 입력받고 싶지 않을 경우
def create(request):
    # request가 POST일 경우
    if request.method == 'POST':
        # if .is_valid (값이 잘 입력 되었는지 확인):
            # 저장하지 않고 model 객체에 접근
            form.save(commit=False)
            # model 객체의 date 변수에 접근

            # model 객체 저장

    ...
```

`html`에 출력하기 (**템플릿 변수** 사용)<br/>
```html
{{ form }}
```

Form안의 내용 어떠한 태그 감싼 채 출력할 미리 결정 가능<br/>
- `{{ form.as_table }}` : `form`의 내용이 `table` 형식으로 출력
- `{{ form.as_p }}` : `form`의 내용이 `p` 형식으로 출력
- `{{ form.as_ul }}` : `form`의 내용이 `ul` 형식으로 출력

<br/>

### 6주차 - 2. form 실습
#### 1. 사용할 앱 내부에 forms.py 생성

#### 2. 필요한 모듈 및 객체 추가
```python
from django import forms
from .model import Blog
```

#### 3. 입력공간 클래스 정의
어떤 `model`을 기반으로 할 것인지<br/>
어떤 데이터를 입력받을 것 인지 `Meta`클래스에 정의
```python
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'body',
        ]

```

#### 4. urls.py에 처리함수 url 생성
```python
urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('search/', views.search, name="search"),
    path('newblog/', views.blogpost, name="newblog"),
]
```

#### 5. views.py에 처리함수 작성
`forms.py`에 작성한 클래스 추가<br/>
```python
from .forms import BlogPost
```

처리함수 작성<br/>
```python
def blogpost(request):
    # 입력된 내용을 처리 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()

            form.save()

            return redirect('home')

    # 빈 페이지 출력 -> GET
    else:
        form = BlogPost()

        return render(request, 'new.html', {
            'form': form,
        })
```
`request`방식이 **POST**일 경우 `form`에 입력된 데이터를<br/>
처리해야 하기 때문에 **POST**방식으로 입력된 내용을 **변수**에 담고<br/>
`is_valid`함수를 이용해 내용이 잘 입력되어있는지 **검사**한 후<br/>
입력되지 않은 나머지 값들을 임의로 입력해 준 후 저장<br/>
`request`방식이 **GET**일 경우 빈 페이지 출력

#### 6. html에 작성한 forms 사용
`as_table` 템플릿 메서드 사용<br/>
`table`형식으로 감싸서 `form` 사용
```html
<form method="POST">
{% csrf_token %}
<table>
    {{ form.as_table }}
</table>
<br>
    <input type="submit" value="제출하기" class="btn btn-dark">
</form>
```

#### 추가 - 임의의 입력공간 생성하기
```python
class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choices=[
        ('1','one'),
        ('2','two'),
        ('3', 'three'),
    ])
```
