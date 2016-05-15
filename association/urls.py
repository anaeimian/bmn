__author__ = 'benyamin'

from django.conf.urls import url

urlpatterns = [
    url(r'requests/$', 'association.views.requests'),
    url(r'details/(?P<app_id>\d+)/$', 'association.views.details'),
    url(r'deleteRequest/$', 'association.views.delete_request'),
    url(r'^$', 'association.views.home'),
]