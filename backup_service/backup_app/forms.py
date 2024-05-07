# backup_app/forms.py
from django import forms
from .models import Backup

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = ['name', 'size_in_mb']  # Campos que aparecerán en el formulario
        labels = {
            'name': 'Nombre del respaldo',
            'size_in_mb': 'Tamaño (MB)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'size_in_mb': forms.NumberInput(attrs={'class': 'form-control'})
        }
