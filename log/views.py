# Create your views here.
from django.shortcuts import render,HttpResponseRedirect

from django.contrib.auth import authenticate, login,logout
from log.forms import *


def log_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/home/')
        else:
            return HttpResponseRedirect('/error/')
    else:
        form  = LoginForm()
        return render(request,'login/login.html',{'form':form})
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/home/')