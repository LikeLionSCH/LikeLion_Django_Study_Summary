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
