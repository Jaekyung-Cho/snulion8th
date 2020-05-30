from django.shortcuts import render
from .models import Feed, Like
from django.shortcuts import redirect
from django.http import HttpResponse
#from django.contrib.auth.models import User 

def home(request):
  if request.method=='POST':
    content = request.POST['content']
    photo =  request.FILES.get('photo', False) #유효성검사 통과를 위한 False
    Feed.objects.create( content=content, author= request.user, photo=photo)
    return redirect('/home/')
  elif request.method=='GET':
    feeds = Feed.objects.all()
    return render(request, 'feedpage/home.html',{'feeds':feeds})

def new(request):
  return render(request, 'feedpage/new.html')