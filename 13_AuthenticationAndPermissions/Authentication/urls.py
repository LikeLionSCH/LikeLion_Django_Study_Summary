from django.contrib import admin
from django.urls import path, include
import userpost.urls
import rest_framework.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpost/', include(userpost.urls)),
    path('api-auth/', include(rest_framework.urls))
]
