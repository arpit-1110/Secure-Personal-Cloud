from __future__ import unicode_literals
from db_file_storage.model_utils import delete_file, delete_file_if_needed

from django.db import models


class FileInfo(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)

class File(models.Model):
    name = models.CharField(max_length=100,blank = True)
    file = models.FileField(upload_to='upload.FileInfo/bytes/filename/mimetype', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    parentfolder = models.ForeignKey('Folder',on_delete=models.CASCADE,blank=True,null=True)

    def save(self, *args, **kwargs):
        delete_file_if_needed(self, 'file')
        super(File, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        delete_file(self, 'file')
        super(File, self).delete(*args, **kwargs)

    def __str__(self):
    	return self.name

class Folder(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE,blank=True,null=True)
	parentfolder = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
	name = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.name

# class Document(models.Model):
# 	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
# 	description = models.CharField(max_length=255, blank=True)
# 	document = models.FileField(upload_to='documents/')
# 	uploaded_at = models.DateTimeField(auto_now_add=True)
# 	location = models.CharField(max_length=1000,blank=True)
