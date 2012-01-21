# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect

from account.forms import UserForm,EditUserForm

def create(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = UserForm()
    return render(request,'account/create.html',{'form':form}) 


def display(request):
    users = User.objects.all()
    return render(request,'account/display.html',{'users':users})


def edit(request):
    if request.method =="POST":
        form = EditUserForm(request.POST,instance = request.user)
        if form.is_valid():
            user = form.save(instance = request.user)
            return HttpResponseRedirect('/home/')
    else:
        form = EditUserForm(instance = request.user )
    return render(request,'account/edit.html',{'form':form})  