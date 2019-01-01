from django import forms

from .models import Registration

class PostForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('firstName', 'lastName', 'age', 'weight', 'rank')