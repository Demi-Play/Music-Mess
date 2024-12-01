from django import forms
from .models import Project, AudioMaterial

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class AudioMaterialForm(forms.ModelForm):
    class Meta:
        model = AudioMaterial
        fields = ['title', 'audio_file']