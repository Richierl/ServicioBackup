# backup_service/urls.py
from django.contrib import admin
from django.urls import path, include
from backup_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backup_app.urls')),  # Incluye las URLs de backup_app
    path('backups/create/', views.create_backup, name='create_backup'),
]
