from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Backup

class BackupListView(ListView):
    model = Backup
    template_name = 'backup_list.html'
    context_object_name = 'backups'

class BackupCreateView(CreateView):
    model = Backup
    fields = ['name', 'data']
    template_name = 'backup_form.html'
    success_url = '/backups/'
# Create your views here.
