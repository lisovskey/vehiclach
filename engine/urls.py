"""
Engine urls
"""

from django.urls import path
from . import views


app_name = 'engine'
urlpatterns = [
    path('',
         views.marks, name='marks'),
    path('add/',
         views.add, name='add'),
    path('<slug:mark_name_slug>/',
         views.models, name='models'),
    path('<slug:mark_name_slug>/<slug:model_name_slug>/',
         views.evos, name='evos'),
]
