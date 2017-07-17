'''
Engine urls
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.marks, name='marks'),
    url(r'^add/$',
        views.add, name='add'),
    url(r'^(?P<mark_name>[A-Z a-z_-]+)/$',
        views.models, name='models'),
    url(r'^(?P<mark_name>[A-Z a-z_-]+)/(?P<model_name>[A-Za-z0-9-]+)/$',
        views.evos, name='evos'),
]
