from django.shortcuts import render
from django.utils import timezone
from .models import File
from django.contrib.auth.models import User

def file_list(request):
    files = File.objects.filter(author=me)
    return render(request, 'upload/file_list.html', {'files': files})