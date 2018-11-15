from django import forms

from upload.models import Document


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