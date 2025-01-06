# blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('django.contrib.auth.urls')),  # Add this line for auth URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)