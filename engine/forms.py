'''
Forms for offers
'''

from django import forms
from . import models

class PropositionForm(forms.ModelForm):
    '''
    Adding a new evo
    '''
    choices = models.Model.objects.order_by('mark', 'name')

    def clean(self):
        evo_name = self.cleaned_data['name'].upper()
        model = self.cleaned_data['model']
        if evo_name in [evo.name for evo in models.Evo.objects.filter(model=model)]:
            raise forms.ValidationError('Evo already exists')

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
                'pattern': models.Evo.name_regex,
            }),
            'year': forms.NumberInput(attrs={
                'class': 'col-12 fix',
                'autocomplete': 'off',
                'min': models.Evo.min_year,
                'max': models.Evo.max_year,
            }),
        }
