from django.conf.urls import include, url


urlpatterns = [
    url(r'messages/ComposeMessage/$', 'manager.views.compose_message'),
    url(r'messages/ComposeMessage/ComposeMessageSubmit/$', 'manager.views.compose_message_submit'),
    url(r'messages/$', 'manager.views.messages'),
    url(r'requests/$', 'manager.views.requests'),

    url(r'faqs/new/$', 'manager.views.new_faq'),
    url(r'faqs/delete/(?P<faq_id>\d+)/$', 'manager.views.delete_faq'),
    url(r'faqs/edit/(?P<faq_id>\d+)/$', 'manager.views.edit_faq'),
    url(r'faqs/$', 'manager.views.faqs'),

    url(r'news/new/$', 'manager.views.new_news'),
    url(r'news/edit/(?P<news_id>\d+)/$', 'manager.views.edit_news'),
    url(r'news/delete/(?P<news_id>\d+)/$', 'manager.views.delete_news'),
    url(r'news/all/$', 'manager.views.news_all'),
    url(r'news/$', 'manager.views.news'),

    url(r'notices/new/$', 'manager.views.new_notice'),
    url(r'notices/edit/(?P<notice_id>\d+)/$', 'manager.views.edit_notice'),
    url(r'notices/delete/(?P<notice_id>\d+)/$', 'manager.views.delete_notice'),
    url(r'notices/all/$', 'manager.views.notices_all'),
    url(r'notices/$', 'manager.views.notices'),

    url(r'facilities/$', 'manager.views.facilities'),
    url(r'facilities/delete/(?P<fac_id>\d+)/$', 'manager.views.delete_facility'),
    url(r'facilities/edit/(?P<fac_id>\d+)/$', 'manager.views.edit_facility'),

    url(r'fields/$', 'manager.views.fields'),
    url(r'fields/delete/(?P<field_id>\d+)/$', 'manager.views.delete_field'),
    url(r'fields/edit/(?P<field_id>\d+)/$', 'manager.views.edit_field'),

    url(r'associations/new/$', 'manager.views.new_association'),
    url(r'associations/delete/(?P<assoc_id>\d+)/$', 'manager.views.delete_association'),
    url(r'associations/edit/(?P<assoc_id>\d+)/$', 'manager.views.edit_association'),
    url(r'associations/(?P<assoc_id>\d+)/$', 'manager.views.get_association'),
    url(r'associations/$', 'manager.views.associations'),

    url(r'logout/$', 'manager.views.logout_user'),
    url(r'^$', 'manager.views.home'),

    url(r'search/$', 'manager.views.ajax_search'),
]