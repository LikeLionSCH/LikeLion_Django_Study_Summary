from django.contrib import admin
from django.urls import path, include
import CBV.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(CBV.urls)),
]
