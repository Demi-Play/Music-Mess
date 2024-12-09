from django import forms
from files.models import File

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file', 'file_type']