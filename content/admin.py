'''
Created on Jan 21, 2012

@author: Jagat
'''
from django.contrib import admin
from content.models import *

admin.site.register(Tag)
admin.site.register(UserTag)
