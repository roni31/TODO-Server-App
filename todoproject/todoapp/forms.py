from django import forms
from .models import Task
from django.forms import ModelForm

class TaskForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task'}),label=False)
    due=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Due Date ..'}),label=False)
    class Meta:
        model=Task
        fields =['title','due']

class UpdateForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Task'}),label=False)

    class Meta:
        model=Task
        fields =['title','due','complete']

