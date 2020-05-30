from django.shortcuts import render
from .models import Feed, Like
from django.shortcuts import redirect
from django.http import HttpResponse
#from django.contrib.auth.models import User 

def home(request):
  feeds = Feed.objects.all()
  return render(request, 'feedpage/home.html',{'feeds':feeds})