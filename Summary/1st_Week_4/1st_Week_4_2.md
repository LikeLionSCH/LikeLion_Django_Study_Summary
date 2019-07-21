## 4주차 - 2. 실습과 강의 중반부 메세지
4주차 - 1. pk, path converter, get_object_or_404 강의<br/>
실습을 이어서 진행하겠습니다.

#### 3. a태그에 템플릿 태그를 사용해 링크 연결하기
`{% url "path" 인자 %}` 형식
```html
<a href="{% url 'detail' blog.id %}"> ...more </a>
```

**완성된 home.html 파일**
```html
{% for blog in blogs.all %}
    <h1> {{ blog.title }} </h1>
    <h3> 날짜 </h3>
    <p> {{ blog.pub_date }} </p>

    <h3> 본문 미리보기 </h3>
    <p>
        {{ blog.summary }}
        <a href="{% url 'detail' blog.id %}"> ...more </a>
    </p>
    <br/>
    <br/>
{% endfor %}
```

#### 4. detail.html 작성하기
`detail.html`에 **템플릿 태그**를 사용해 본문 내용 출력

```html
<h1> {{ blog.title }} </h1>
<h3> 날짜 </h3>
<p> {{ blog.pub_date }} </p>

<h3> 본문 내용 </h3>
<p>
    {{ blog.body }}
</p>
```

### 결과 화면
**home.html**<br/>
<img src="../1st_images/Week_4_2_Test_Image_1.png" width="600" height="auto">

**detail.html**<br/>
<img src="../1st_images/Week_4_2_Test_Image_2.png" width="600" height="auto">

**404 Not Found**<br/>
<img src="../1st_images/Week_4_2_Test_Image_3.png" width="600" height="auto">

### 추가 내용
1. **복습을 합시다!**
2. **오류와 에러는 성장 가능성이다!**
    - **답답해하지 말자!**
    - **당당해지자!**
    - **질문 하자!**
