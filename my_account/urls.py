# from django.conf.urls import patterns, url
from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       # url(r'^$', 'monitor.views.index',name='index'),
                       url(r'^show_all/$', 'my_account.views.show_all', name='show_all'),
                       url(r'^new_account/$', 'my_account.views.new_account', name='new_account'),
                       )
