 
from django.contrib import admin
from django.urls import include,path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hawkeye/', include('hawkeye.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/hawkeye/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.DEPLOYMENT_URL, document_root=settings.DEPLOYMENT_ROOT)
