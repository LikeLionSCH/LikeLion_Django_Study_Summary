from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Album import views

router = DefaultRouter()
router.register('', views.AlbumViewSet)

urlpatterns = [
    path('', include(router.urls))
]
