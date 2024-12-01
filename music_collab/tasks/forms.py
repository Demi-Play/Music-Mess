from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assignee', 'status', 'due_date']

        widgets = {
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',  # Используем тип datetime-local для ввода даты и времени
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'assignee': forms.Select(attrs={
                'class': 'form-control',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }