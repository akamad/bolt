from django.conf.urls.defaults import patterns, include, url
import os
from settings import SITE_ROOT
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bolt.views.home', name='home'),
    # url(r'^bolt/', include('bolt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

from settings import OUR_APPS

for aps in OUR_APPS:
    urlpatterns += patterns('',
  
     url(r'^'+aps+'/', include(aps+'.urls')),
     )
    
    

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(SITE_ROOT, 'templates/media')}),
                        )