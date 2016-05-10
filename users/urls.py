from django.conf.urls import url


urlpatterns = [

    url(r'logout/$', 'users.views.logout_view'),
    url(r'register/$', 'users.views.user_register'),
    url(r'messages/$', 'users.views.get_user_messages'),
    url(r'requests/edit/(?P<application_id>\d+)/$', 'users.views.edit_coop_request'),
    url(r'requests/delete/(?P<application_id>\d+)/$', 'users.views.delete_coop_request'),
    url(r'requests/preview/coop/(?P<application_id>\d+)/$', 'users.views.preview_coop_request'),
    url(r'requests/new/coop/$', 'users.views.new_coop_request'),

    url(r'requests/new/cons/$', 'users.views.new_military_request'),

    url(r'requests/new/$', 'users.views.new_request'),
    url(r'requests/view/(?P<application_id>\d+)/$', 'users.views.view_coop_request'),


    url(r'requests/$', 'users.views.user_requests'),

    url(r'getassocs/$', 'users.views.getassocs'),

    url(r'$', 'users.views.user_login'),
]