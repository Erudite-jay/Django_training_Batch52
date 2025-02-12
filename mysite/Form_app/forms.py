from django import forms
from .models import FileUpload

# class FileUploadForm(forms.Form):
    # name=forms.CharField(max_length=100)
    # file=forms.FileField()

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['name', 'file']