from django.contrib import admin
from django.urls import path, include
import userpost.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userpost/', include(userpost.urls))
]
