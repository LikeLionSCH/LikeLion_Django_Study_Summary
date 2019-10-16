from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import UserPostViewSet

router = DefaultRouter()
router.register('', UserPostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
