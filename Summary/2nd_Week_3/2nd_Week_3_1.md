## 3주차 - 1. View of DRF

### 작성했었던 views.py

**모델**기반의 `viewset`을 작성했었다.<br>

```python
from rest_framework import viewsets
from .models import Post
from .serializer import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### ViewSet

**View**(**CRUD**)를 설계하는 가장 간단한 방법<br>

#### View를 배우는 과정

1. APIView
2. Mixins
3.  Generic CBV
4.  ViewSet

점차 **View**를 **간략**하게 **설계**하는 방법을 배운다.<br>

