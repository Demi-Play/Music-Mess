from django import forms
from .models import AudioComment

class AudioCommentForm(forms.ModelForm):
    class Meta:
        model = AudioComment
        fields = ['file', 'timestamp', 'text']