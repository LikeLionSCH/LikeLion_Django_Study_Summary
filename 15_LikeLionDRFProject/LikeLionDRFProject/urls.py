from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from .schema_view import schema_view
import rest_framework.urls
import File.urls
import Album.urls
import Essay.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('file', include(File.urls)),
    path('album', include(Album.urls)),
    path('essay', include(Essay.urls)),
    path('api-auth/', include(rest_framework.urls))
]

if settings.DEBUG:
    urlpatterns = [
        re_path(r'^swagger(?P<format>.json|.yaml)$',
                schema_view.without_ui(cache_timeout=0),
                name='schema-json'),
        path("swagger/",
             schema_view.with_ui('swagger', cache_timeout=0),
             name='schema-swagger-ui'),
        path("docs/",
             schema_view.with_ui('redoc', cache_timeout=0),
             name='schema-redoc'),
    ] + urlpatterns
