"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
"""
from django.urls import path, include
from .views import BackupListView, BackupCreateView

urlpatterns = [
    path('backups/', BackupListView.as_view(), name='backup_list'),
    path('backups/create/', BackupCreateView.as_view(), name='backup_create'),
]
