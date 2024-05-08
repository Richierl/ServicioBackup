from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('backups/', views.backup_list, name='backup_list'),
    path('backups/create/', views.backup_create, name='backup_create'),
    path('backups/<int:backup_id>/delete/', views.delete_backup, name='delete_backup'),
]
