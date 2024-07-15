from django import forms
from django.forms import ModelForm

from .models import *

class taskForm(forms.ModelForm):

    # Sets the placeholder value
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = task
        fields = '__all__'