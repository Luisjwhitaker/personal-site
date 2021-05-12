from django import forms
from django.forms import ModelForm

from .models import *

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
