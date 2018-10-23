from __future__ import unicode_literals

from django.db import models


class File(models.Model):
	# author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	description = models.CharField(max_length=255, blank=True)
	document = models.FileField(upload_to='documents/')
	# uploaded_at = models.DateTimeField(auto_now_add=True)