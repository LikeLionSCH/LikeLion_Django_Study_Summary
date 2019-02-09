from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import blogapp.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio', portfolio.views.portfolio, name="portfolio"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
