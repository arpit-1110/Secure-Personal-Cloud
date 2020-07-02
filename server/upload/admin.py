from django.contrib import admin
from .models import Folder,File,FileInfo

# admin.site.register(Document)
admin.site.register(Folder)
admin.site.register(File)
admin.site.register(FileInfo)