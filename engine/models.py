"""
Engine models
"""

from django.db import models
from datetime import datetime
from django.core.validators import (MinValueValidator,
                                    MaxValueValidator,
                                    RegexValidator)


class Mark(models.Model):
    """
    Mark of an auto
    """
    name_regex = r'^[A-z 0-9]+$'
    country_regex = r'^[A-z ]+$'

    name = models.CharField('mark', unique=True, max_length=14, validators=(
        RegexValidator(name_regex, message='Invalid mark name'),
    ))
    country = models.CharField('country', max_length=14, validators=(
        RegexValidator(country_regex, message='Invalid country'),
    ))

    def name_slug(self):
        return self.name.replace(' ', '_')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'


class Model(models.Model):
    """
    Model of an auto
    """
    name_regex = r'^[A-z 0-9]+$'
    kind_regex = r'^[A-z]+$'

    name = models.CharField('model', max_length=14, validators=(
        RegexValidator(name_regex, message='Invalid model name'),
    ))
    kind = models.CharField('kind', max_length=1, validators=(
        RegexValidator(kind_regex, message='Invalid kind'),
    ))
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE)

    def clean(self):
        self.kind = self.kind.upper()

    def name_slug(self):
        return self.name.replace(' ', '_')

    def __str__(self):
        return f'{self.mark.name} {self.name}'

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'


class Evo(models.Model):
    """
    Evolution of Model of an auto
    """
    name_regex = r'^[A-z0-9]+$'
    year_min = 1800
    year_max = datetime.now().year + 1

    name = models.CharField('evo', max_length=8, validators=(
        RegexValidator(name_regex, message='Invalid evo name'),
    ))
    year = models.IntegerField('year', validators=(
        MinValueValidator(year_min, message='Invalid year'),
        MaxValueValidator(year_max, message='Invalid year'),
    ))
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def clean(self):
        self.name = self.name.upper()

    def __str__(self):
        return f'{self.model.mark.name} {self.model.name} {self.name}'

    class Meta:
        verbose_name = 'Evolution'
        verbose_name_plural = 'Evolutions'
