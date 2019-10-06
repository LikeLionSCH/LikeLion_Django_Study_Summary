# 데이터 처리 대상
from CBV.models import Post
from CBV.serializer import PostSerializer
# status에 따라서 직접 Response를 처리할 것
from django.http import Http404  # Get Object or 404 직접 구현
from rest_framework.response import Response
from rest_framework import status
# APIView를 상속받은 CBV
from rest_framework.views import APIView


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        # 다수의 객채를 직렬화 할때 many=True
        serializer = PostSerializer(posts, many=True)

        # 직접 Response 반환해주기 : serializer.data
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)

        # 직접 유효성 검사 진행 후 저장
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# PostList 클래스와는 다르게 pk값을 받는다.
class PostDetail(APIView):
    # get_object_or_404를 구현해주는 helper function
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        # post = get_object_or_404(Post, pk)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
