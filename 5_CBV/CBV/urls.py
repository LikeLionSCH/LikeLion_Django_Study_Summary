from django.contrib import admin
from django.urls import path, include
import classBaseCrud.urls
import classBaseCrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(classBaseCrud.urls)),
]
