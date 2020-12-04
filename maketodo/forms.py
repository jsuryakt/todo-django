from django import forms
from django.db import models
from .models import ToDo

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['todo_text']
        widgets = {'todo_text': forms.TextInput(attrs={
                                        'class': 'form-control',
                                        'placeholder':'Add Your Todo!'})}
