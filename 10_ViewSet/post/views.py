from .models import Post
from .serializer import PostSerializer
from rest_framework import viewsets
from django.http import HttpResponse

# @action 처리
from rest_framework import renderers
from rest_framework.decorators import action


# ListView, DetailView의 조회만 가능
# class PostViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# ListView, DetailView에 대한 CRUD모두 가능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # @action(method=['post])
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        # @action Custion API Test를 띄우는 Custom API
        return HttpResponse("@action Custom API Test")
