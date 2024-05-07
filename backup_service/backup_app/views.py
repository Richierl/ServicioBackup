# backup_app/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Backup
from .forms import BackupForm

def backup_list(request):
    backups = Backup.objects.all()
    return render(request, 'backup_list.html', {'backups': backups})

def backup_create(request):
    if request.method == 'POST':
        form = BackupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/backups/')  # Redirigir a la lista de respaldos después de crear uno
    else:
        form = BackupForm()
    return render(request, 'backup_form.html', {'form': form})

def home(request):
    # Aquí puedes realizar consultas u operaciones necesarias antes de renderizar la página
    backups = Backup.objects.all()  # Ejemplo de consulta a todos los backups

    # Renderiza la página principal con la lista de backups
    return render(request, 'home.html', {'backups': backups})