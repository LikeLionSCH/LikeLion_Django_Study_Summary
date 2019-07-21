## 5주차 - 4. Pagination 실습

### 1. 필요한 모듈 import
```python
from django.core.paginator import Paginator
```

### 2. views.py의 home함수 수정하기
```python
def home(request):
    blog_list = Blog.objects.all()

    paginator = Paginator(blog_list, 3)
    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, "home.html", {
        "posts": posts,
    })
```

### 3. home.html 수정
기존에는 `all`매서드를 사용해 모든 객체를 가져와 사용<br/>
**Pagination** 기능을 사용하면 한 페이지씩 포스트를 가져와 사용
```html
{% for blog in posts %}
...
{% endfor %}
```

페이지 이동 링크 추가
```html
{% if posts.has_previous %}
<a href="?page=1">First</a>
<a href="?page={{ posts.previous_page_number }}"> Previous</a>
{% endif %}

<span> {{ posts.number }} </span>
<span> of </span>
<span> {{ posts.paginator.num_pages }} </span>

{% if posts.has_next %}
<a href="?page={{ posts.next_page_number }}"> Next</a>
<a href="?page={{ posts.paginator.num_pages }}"> Last</a>
{% endif %}
```
