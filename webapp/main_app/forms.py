# forms.py

from django import forms
from .models import WordPair

class WordPairForm(forms.ModelForm):
    class Meta:
        model = WordPair
        fields = ['word', 'translation',]

        widgets = {
            'word': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 500px;',
            }),

            'translation': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 500px;',
            }),

        }
