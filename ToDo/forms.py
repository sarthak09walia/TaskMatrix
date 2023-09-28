from django import forms
from .models import Todo

class ToDo_Create(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'due_date': forms.TextInput(attrs={'type': 'date'}),
        }