from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
import manager

urlpatterns = [
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^manager/', include('manager.urls')),
                  url(r'^plans/$', 'common.views.plans'),
                  url(r'^intro/$', 'common.views.intro'),
                  url(r'^association/', include('association.urls')),
                  url(r'^plans/$', 'common.views.plans'),
                  url(r'^intro/$', 'common.views.intro'),
                  url(r'^users/cons/', include('cons.urls')),
                  url(r'^users/', include('users.urls')),
                  url(r'^intro/$', 'common.views.intro'),
                  url(r'^$', 'common.views.home'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
