__author__ = 'benyamin'

from django.conf.urls import url

urlpatterns = [
    url(r'^news/$', 'association.views.news'),
    url(r'^notices/$', 'association.views.notices'),
    url(r'requests/$', 'association.views.requests'),
    url(r'deleteNew/$', 'association.views.delete_new'),
    url(r'^$', 'association.views.home'),
]