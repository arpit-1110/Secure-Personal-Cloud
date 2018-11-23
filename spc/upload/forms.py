from django import forms
from django.urls import reverse_lazy

from upload.models import File,Folder
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# from upload.models import 
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['author','parentfolder','name','md5sum']
        widgets = {
            'picture': DBClearableFileInput
        }

class FileFormAPI(forms.ModelForm):
    class Meta:
        model = File
        exclude = ['author','parentfolder']
        widgets = {
            'picture': DBClearableFileInput
        }

class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields = ('name',)

class SearchForm(forms.Form):
	search = forms.CharField(label='search', max_length=1000)

# class FileDelete(DeleteView):
#     model = File #for what this view is for
#     success_url = reverse_lazy('home')


# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('author','description', 'document','location')
#         # fields = ('description', 'document','location')



# class DocumentForm(forms.Form):
#     id = forms.IntegerField(required=False, widget=forms.HiddenInput())
#     description = forms.CharField(max_length=255)
#     documnet = forms.FileField()
#     location = forms.CharField(max_length=255)