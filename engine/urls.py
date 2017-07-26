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
    url(r'^(?P<url_mark_name>[^\s/]+)/$',
        views.models, name='models'),
    url(r'^(?P<url_mark_name>[^\s/]+)/(?P<url_model_name>[^\s/]+)/$',
        views.evos, name='evos'),
]
