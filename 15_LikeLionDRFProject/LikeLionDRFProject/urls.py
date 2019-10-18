from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from .schema_view import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [
        re_path(r'^swagger(?P<format>.json|.yaml)$',
                schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path("swagger/",
             schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path("docs/",
             schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ] + urlpatterns
