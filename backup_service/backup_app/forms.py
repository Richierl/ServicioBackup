# backup_app/forms.py
from django import forms
from .models import Backup

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = ['name', 'description', 'file']  # Incluir el campo 'file' para subir archivos
