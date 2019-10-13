## 3주차 - 6. Router

### 기존의 URL 설정 방식

아래와 같은 방법으로 설정했던 `URL`이 어떻게 `Router`까지<br>
발전해서 사용되어 왔는지에 대해서 알아보자.<br>

```python
urlpatterns = [
    path(...)
    ...
]
```

### ViewSet 복습

#### ReadOnlyModelViewSet

-   `retrieve()`와 `list()`의 기능

#### ModelViewSet

-   `list()`, `create()`, `retrieve()`, `update()`
    <br>`partial_update()`, `destroy()`의 기능

### Path

위의 `ViewSet`을 하나의 `path`함수만으로 처리가 가능할까?<br>
하나의 `path`로 `ListView`, `DetailView`의 **CRUD**가 모두 처리가 가능한가?<br>
**불가능**하다. 필연적으로 2개 이상의 `path`가 필요하다.<br>
`path`를 하나로 묶어(~~**path함수의 두 번쨰 인자의 함수를 묶는다**~~)줄 방법이 필요로 한다.<br>

### path()를 묶어주는 as_view()

#### as_view 함수 구성

```python
as_view({'http_method' : '처리할 함수'})
```

#### 예시

아래와 같이 `as_view`함수를 작성하고 `urlpatterns`에 넣어주면 잘 작동한다.<br>
자세한 내용은 [Django REST framework 공식문서](https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/)에서 확인 가능하다.<br>

```python
path = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', path)
]
```

### Router

위에서 작성했던 관례적인 `URL` **맵핑 단계**를 **자동**으로 **구현**해주는 방식<br>

#### 사용방법

1. `rest_framework`의 `router`에서 `DefaultRouter` 추가

```python
from rest_framework.router import DefaultRouter
```

2. `DefaultRouter`객체 생성 및 등록

`URL Prefix`는 `127.0.0.1:8000/post`와 같은 `URL`에서 `post`부분 이다.<br>

```python
router = DefaultRouter()
router.register(<URL Prefix>, <View Logic>)
```

3. `urlpatterns`에 `router`의 `urls` 추가

```python
urlpatterns = [
    path('', include(router.urls)),
]
```
