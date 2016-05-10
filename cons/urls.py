from cons import views
from django.conf.urls import url

urlpatterns = [
    url(r'education/$', views.education),
    url(r'teaching/$', views.teaching_experience),
    url(r'intlpapers/$', views.international_papers),
    url(r'research/$', views.research),
    url(r'intrnlpapers/$', views.internal_papers),
    url(r'confpapers/$', views.confpapers),
    url(r'intrnlinventions/$', views.internal_inventions),
    url(r'intlinventions/$', views.international_inventions),
    url(r'rankings/$', views.rankings),
    url(r'olympiads/$', views.olympiads),
    url(r'scholarships/$', views.scholarships),
    url(r'grants/$', views.grants),
    url(r'postdoc/$', views.postdoc),
    url(r'offers/$', views.offers),
    url(r'memberships/$', views.memberships),
    url(r'editors/$', views.editors),
    url(r'notes/$', views.notes),
    url(r'submit/$', views.submit),
    url(r'app/$', views.app),
    url(r'$', views.dashboard),
]
