from rest_framework.routers import DefaultRouter
from django.urls import path, include
from File import views

router = DefaultRouter()
router.register('', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]
