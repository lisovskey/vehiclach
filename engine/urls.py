'''
Engine urls
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<mark_name>[A-Z a-z]+)/$', views.sub_index, name='subindex'),
    url(r'^(?P<mark_name>[A-Z a-z]+)/(?P<model_name>[A-Za-z0-9]+)/$',
        views.sub_sub_index, name='subsubindex'),
]
