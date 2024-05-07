# backup_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # URL para la pagina principal
    path('backups/', views.backup_list, name='backup_list'),  # URL para la lista de respaldos
    path('backups/create/', views.backup_create, name='backup_create'),  # URL para el formulario de creación de respaldo
]
