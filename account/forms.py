'''
Created on Jan 21, 2012

@author: Jagat
'''
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password','email')
        
class EditUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','email')