'''
Defenition of models
'''

from django.db import models

class Mark(models.Model):
    '''
    Mark of an auto
    '''
    name = models.CharField("mark", unique=True, max_length=14)
    country = models.CharField("country", max_length=14)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'

class Model(models.Model):
    '''
    Model of an auto
    '''
    name = models.CharField("model", max_length=14)
    kind = models.CharField("kind", max_length=1)
    mark = models.ForeignKey(Mark)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        verbose_name_plural = 'Models'

class Evo(models.Model):
    '''
    Evolution of Model of an auto
    '''
    name = models.CharField("evo", max_length=14)
    year = models.IntegerField("year")
    model = models.ForeignKey(Model)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Evolution'
        verbose_name_plural = 'Evolutions'
