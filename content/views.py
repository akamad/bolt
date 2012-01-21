# Create your views here.
from django.shortcuts import render,HttpResponseRedirect

from content.forms import *
from content.models import Tag

def create(request):
    if request.method =="POST":
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit = False)
            if request.user:
                tag.owner = request.user
                tag.save()
            return HttpResponseRedirect('/home/')
    else:
        form = TagForm()
    return render(request,'content/tag/create.html',{'form':form}) 


def display(request):
    tags = Tag.objects.get(owner = request.user)
    return render(request,'content/tag/display.html',{'tags':tags})


def edit(request,id):
    id = int(id)
    tag = Tag.objects.get(id = id)
    if request.method =="POST":
        form = TagForm(request.POST,instance = tag)
        if form.is_valid():
            user = form.save(instance = tag)
            return HttpResponseRedirect('/home/')
    else:
        form = TagForm(instance = tag )
    return render(request,'content/tag/edit.html',{'form':form})  

def delete(request,id):
    id = int(id)
    tag = Tag.objects.get(id = id)
    tag.delete()
    return HttpResponseRedirect('/home/')