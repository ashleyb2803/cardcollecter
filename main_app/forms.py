from django import forms
from .models import Wrestler

class WrestlerForm(forms.ModelForm):
    class Meta:
        model = Wrestler
        fields = ['name', 'nickname', 'debut_year', 'championships_won', 'signature_move']
        widgets = {
            'debut_year': forms.NumberInput(attrs={'min': 1900, 'max': 2023}),
            'championships_won': forms.NumberInput(attrs={'min': 0}),
        }

