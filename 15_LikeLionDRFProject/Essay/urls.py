from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Essay import views

router = DefaultRouter()
router.register('', views.EssayViewSet)

urlpatterns = [
    path('', include(router.urls))
]
