from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # URL de la página principal
    path('backups/', views.backup_list, name='backup_list'),  # URL para listar respaldos
    path('backups/create/', views.create_backup, name='backup_create'),  # URL para el formulario de creación de respaldo
]
