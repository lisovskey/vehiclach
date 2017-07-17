'''
Forms for offers
'''

from django import forms
from . import models

class PropositionForm(forms.ModelForm):
    '''
    Adding a new evo
    '''
    class Meta:
        model = models.Evo
        fields = [
            'model',
            'name',
            'year',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'col-12 fix',
                'autocomplete': 'off',
            }),
            'year': forms.NumberInput(attrs={
                'class': 'col-12 fix',
                'autocomplete': 'off',
            }),
        }

    choices = models.Model.objects.order_by('mark')
