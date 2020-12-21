from django import forms
from django.forms import ModelForm
from .models import dialecticapp

class DialecticAppForm(forms.ModelForm):
    class Meta: #inner Class / container
        model=dialecticapp
        fields=[
    'night',
    'morning',
    'daytime',
    'evening',
    'beforeSleep',
    'notes',
    ]
