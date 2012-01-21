'''
Created on Jan 21, 2012

@author: Jagat
'''
from content.models import Tag 
from django import forms
from django.forms import ModelForm

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ('name','description')
        
