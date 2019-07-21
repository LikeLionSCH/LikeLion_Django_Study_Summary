## 6주차 - 1. form 이론

### Form(입력공간)
**Model**형식에 맞는 **Form**만들기<br/>
`html`로 만드는 것은 **한계**가 존재

### forms.py
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
