from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
    title="Like Lion REST API",
    default_version='v1',
    description='''<h3>🦁 Like Lion 7th Django restframework Project.</h3>
    The `swagger-ui` view can be found [here](http://127.0.0.1:8000/swagger/)
    The `ReDoc` view can be found [here](http://127.0.0.1:8000/docs/)
    The swagger YAML document can be found [here](http://127.0.0.1:8000/swagger.yaml)
    ''',
    contact=openapi.Contact(email="alstn2468_@naver.com"),
    license=openapi.License(name="MIT License"),
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)
