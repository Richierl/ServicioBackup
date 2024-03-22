from django.urls import path
from .views import BackupListView, BackupCreateView

urlpatterns = [
    path('backups/', BackupListView.as_view(), name='backup_list'),
    path('backups/create/', BackupCreateView.as_view(), name='backup_create'),
]