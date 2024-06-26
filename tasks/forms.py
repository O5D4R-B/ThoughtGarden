from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': '#aqui va la clase de react'}),
            'description': forms.Textarea(attrs={'class': '#aqui va la clase de react'}),
        }
