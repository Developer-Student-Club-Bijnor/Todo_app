from django import forms
from django.forms import ModelForm
from django.forms import fields
from django.forms.widgets import TextInput
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=TextInput(
        attrs={"placeholder": "Add new task..."}))

    class Meta:
        model = Task
        fields = '__all__'
