# backup_service/urls.py
from django.contrib import admin
from django.urls import path, include
from backup_app import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backup_app.urls')),  # Incluye las URLs de backup_app
    path('backups/create/', views.backup_create, name='backup_create'),
]

# Configurar las URL para servir archivos de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)