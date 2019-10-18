from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Like Lion REST API",
        default_version='v1',
        description="🦁Like Lion 7th DRF Project.",
        contact=openapi.Contact(email="alstn2468_@naver.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^swagger(?P<format>.json|.yaml)$",
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path("swagger/",
         schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("redoc/",
         schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
