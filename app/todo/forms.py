from django import forms
from .models import list



class formList(forms.ModelForm):
    class Meta:
        model = list
        fields = ['item', 'completed']
