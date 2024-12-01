from django import forms
from .models import Message, Chat

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'message_type']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['project']  # Укажите необходимые поля для создания чата