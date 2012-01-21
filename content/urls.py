'''
Created on Jan 21, 2012

@author: Jagat
'''
from django.conf.urls.defaults import *


urlpatterns = patterns('content.views',
    # Uncomment the next line to enable the admin:
     (r'^tag/create/$', 'create'),
     (r'^tag/display/$', 'display'),
     (r'^tag/edit/$', 'edit'),
     (r'^tag/delete/$', 'delete'),
)
