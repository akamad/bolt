'''
Created on Jan 21, 2012

@author: Jagat
'''
from django.conf.urls.defaults import *


urlpatterns = patterns('log.views',
    # Uncomment the next line to enable the admin:
     (r'^in/$', 'log_in'),
     (r'^out/$', 'logout_user'),
     
)
