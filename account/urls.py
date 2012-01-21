'''
Created on Jan 21, 2012

@author: Jagat
'''
from django.conf.urls.defaults import *


urlpatterns = patterns('account.views',
    # Uncomment the next line to enable the admin:
     (r'^create/$', 'create'),
     (r'^display/$', 'display'),
     (r'^edit/$', 'edit'),
)
