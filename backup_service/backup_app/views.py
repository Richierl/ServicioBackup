from django.shortcuts import render, redirect
from .models import Backup
from .forms import BackupForm

def home(request):
    backups = Backup.objects.all()
    return render(request, 'home.html', {'backups': backups})

def create_backup(request):
    if request.method == 'POST':
        form = BackupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('backup_list')  # Redirige a la lista de respaldos
    else:
        form = BackupForm()
    return render(request, 'backup_form.html', {'form': form})

def backup_list(request):
    backups = Backup.objects.all()
    return render(request, 'backup_list.html', {'backups': backups})
