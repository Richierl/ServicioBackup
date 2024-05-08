from django.shortcuts import render, redirect, get_object_or_404
from .forms import BackupForm
from .models import Backup

def home(request):
    backups = Backup.objects.all()
    return render(request, 'home.html', {'backups': backups})

def backup_list(request):
    backups = Backup.objects.all()
    return render(request, 'backup_list.html', {'backups': backups})

def backup_create(request):
    if request.method == 'POST':
        form = BackupForm(request.POST, request.FILES)
        if form.is_valid():
            # Guardar el formulario sin commit para poder manipular el objeto
            backup = form.save(commit=False)
            
            # Calcular el tamaño del archivo en MB
            if 'file' in request.FILES:
                file_size_mb = request.FILES['file'].size / (1024 * 1024)  # Convertir a MB
                backup.size_in_mb = round(file_size_mb, 2)  # Redondear a 2 decimales
            
            # Guardar el objeto Backup con el tamaño calculado
            backup.save()
            return redirect('backup_list')
    else:
        form = BackupForm()
    return render(request, 'backup_form.html', {'form': form})

def delete_backup(request, backup_id):
    # Obtener el backup por su ID o devolver un error 404 si no existe
    backup = get_object_or_404(Backup, pk=backup_id)

    if request.method == 'POST':
        # Si se recibió una solicitud POST, eliminar el backup
        backup.delete()
        return redirect('backup_list')  # Redirigir a la lista de backups

    # Si no es una solicitud POST, renderizar una plantilla de confirmación de eliminación
    return render(request, 'backup_delete_confirm.html', {'backup': backup})