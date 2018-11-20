from django import forms

from upload.models import File,Folder,Document


# from upload.models import 
from db_file_storage.form_widgets import DBClearableFileInput
from django import forms

class FileForm(forms.ModelForm):
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

class FileDelete(DeleteView):
    model = File #for what this view is for
    success_url = reverse_lazy('home')


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('author','description', 'document','location')
        # fields = ('description', 'document','location')



# class DocumentForm(forms.Form):
#     id = forms.IntegerField(required=False, widget=forms.HiddenInput())
#     description = forms.CharField(max_length=255)
#     documnet = forms.FileField()
#     location = forms.CharField(max_length=255)