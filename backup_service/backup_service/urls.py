# backup_service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backup_app.urls')),  # Incluye las URLs de backup_app
]
