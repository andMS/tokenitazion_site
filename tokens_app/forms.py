from django import forms

from .models import Get

class PostForm(forms.ModelForm):

    class Meta:
        model = Get
        fields = ('token')
