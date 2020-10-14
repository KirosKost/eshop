from django import forms
from .models import Applications
from django.db import models


class ApplicationsForm(forms.ModelForm):
    class Meta:
        model = Applications
        fields = ['mail', 'name', 'comment']
