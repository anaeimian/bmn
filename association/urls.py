__author__ = 'benyamin'

from django.conf.urls import url

urlpatterns = [

    url(r'requests/$', 'association.views.requests'),
    url(r'deleteNew/$', 'association.views.delete_new'),
    url(r'home/$', 'association.views.home'),
]