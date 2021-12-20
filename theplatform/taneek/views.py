from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib import messages
import sqlite3
from taneek.models import *
from taneek.models import displayusername
from accounts.views import *
from django.http import HttpResponseRedirect, request
from .forms import *
from django.db.models import Q



def Home(request):
    return render(request, 'index.html')

def Connections(request):
    post1 = Posts.objects.all()
    context = {'post1': post1}
    return render(request, 'Connections.html',context)

def About(request):
    return render(request, 'about.html')

def about_edit(request):
    return render(request, 'about_edit.html')

def search(request):
    displaynames = User.objects.all()
    return render(request, 'search.html',{"displayusernames":displaynames})



def search_username(request):
    query = request.GET.get('query','')
    S_user = User.objects.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(email__icontains=query))
    return render(request,'search_username.html',{"query": query , "S_user": S_user})

def connecteduser(request):
    return render(request, 'connecteduser.html')

def post(request):
    current_user = request.user
    p = User.objects.filter(id =current_user.id)
    imageuploader_profile = Posts.objects.filter(imageuploader_profile=p).all()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            p=post.imageuploader_profile
            post.save()
            return HttpResponseRedirect('/Connections')
    else:
        form = PostForm()
    return render(request,'post.html',{'form':form})

def penord(request):
    if request.method == "POST":
        x = request.POST.get('id')
        ConnectedUser.objects.filter(id=x).update(status="Complete")
        print(x, " complete")
        return redirect(connecteduser)

