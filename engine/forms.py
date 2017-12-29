"""
Forms for offers
"""

from django import forms
from . import models


class PropositionForm(forms.ModelForm):
    """
    Adding a new evo
    """
    choices = models.Model.objects.order_by('mark__name', 'name')

    def clean(self):
        evo_name = self.cleaned_data['name'].upper()
        model = self.cleaned_data['model']
        if evo_name in [evo.name for evo in model.evo_set.all()]:
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
                'min': models.Evo.year_min,
                'max': models.Evo.year_max,
            }),
        }
