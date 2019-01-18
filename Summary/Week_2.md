### 2주차 - 1.wordcount 이론

#### 유의사항
1. 서로서로 질문하자!<br/>
2. 질문을 **부끄러워** 하지 말자!

#### Word Count
긴 글을 입력했을 때 사용된 **단어의 수**를 반환하는 기능<br/>
해당 강의는 일단 `HTML`로만 구현<br/>
`HTML`은 디자인 하는 언어가 아니다.<br/>
`CSS`등으로 꾸미는 것은 각자 알아서.

#### 이용자의 눈으로 본 Wordcount
1. `home`에서 링크 클릭
    - About 페이지 출력

2. home에서 글 작성 후 제출 버튼 클릭
    - 글자의 개수가 출력

#### Django의 눈으로 본 Wordcount
1. 사용자가 처음 홈페이지에 들어온 경우
    - `home` 페이지 출력
2. 사용자가 링크를 클릭했을 경우
    - 미리 준비해논 `About` 페이지 출력
3. 사용자가 글을 작성한 후 제출 버튼 클릭
    - 사용자가 입력한 데이터를 함수로 처리한 후<br/>결과를 나타내는 페이지 출력

#### 우리가 만들어야 하는 HTML
1. home.html
    - 처음 들어왔을 때 보여지는 페이지
2. about.html
    - 정보를 보여주는 페이지
3. result.html
    - 결과를 보여주는 페이지

#### 각 페이지의 기능
**home.html**
1. `about`페이지와 링크로 연결
2. 사용자들로부터 입력 처리
3. 입력 받은 결과 제출 버튼

**about.html**
1. `home`페이지와 링크로 연결
2. `About`에 관한 정보 저장

**result.html**
1. `home`에서 입력받은 데이터를 처리할<br/>함수를 받아 결과 출력

#### 만들어야 하는 함수 (views.py)
**views.py**<br/>
**정보**를 **어떤** 상황에서 **어떻게** 처리할지 결정할 함수를 포함

정의할 함수
1. `home`을 띄우는 함수
    ```python
    def home(request):
        ...
        return render(request, home.html)
    ```
2. `about`을 띄우는 함수
    ```python
    def about(request):
        ...
        return render(request, about.html)
    ```
3. `result`에 전달할 함수
    - `home`에서 입력받은 데이터 처리 함수
    - 글자를 세 주는 함수

#### 만들어야 하는 URL
1. `home`을 띄우는 `url`
    - 뒤에 아무것도 붙지않는 `url`
2. `about`을 띄우는 `url`
    - 뒤에 `/about`이 붙는 `url`
3. `result`를 띄우는 `url`
    - 뒤에 `/result`가 붙는 `url`

#### 템플릿 언어
`HTML`안에 쓰는 `Django` 제공 언어<br/>
`HTML`안에 파이썬 변수/문법을 쓸 때 사용

**템플릿 변수**<br/>
```
{{python_variable}}
```
해당 파이썬 변수(`python_variable`)를 `HTML`파일에 담아 출력

**템플릿 필터**<br/>
```
{{python_value | filter}}
```
템플릿 변수에 추가적인 속성 및 기능 제공

예시<br/>
- value의 길이 반환
```
{{value | length}}
```
- value를 소문자로 출력
```
{{value | lower}}
```

**템플릿 태그**<br/>
```
{% tag %} ... {% endtag %}
```
`HTML`상에서 파이썬 문법 사용<br/>
`url`생성 등의 기능 제공, **닫는 태그 필요**

**템플릿 태그 예시**<br/>
Python
```python
Aclass = ["민철", "철수", "영희"]
```

HTML
```html
number_of_students = {{class | length}}
{% for students in Aclass %}
    {{students}}
{% endfor %}
```

URL 생성
```html
{% url 'url_name' %}
```

**알아두면 좋은 것**<br/>
템플릿 상속 : [링크](http://rednooby.tistory.com/94)
