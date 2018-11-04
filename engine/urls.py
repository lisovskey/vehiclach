"""
Engine urls
"""

from django.urls import path
from .views import MarkListView, EvoCreateView, ModelListView, EvoListView


app_name = 'engine'
urlpatterns = [
    path('',
         MarkListView.as_view(), name='marks'),
    path('add/',
         EvoCreateView.as_view(), name='add'),
    path('<slug:mark_slug>/',
         ModelListView.as_view(), name='models'),
    path('<slug:mark_slug>/<slug:model_slug>/',
         EvoListView.as_view(), name='evos'),
]
