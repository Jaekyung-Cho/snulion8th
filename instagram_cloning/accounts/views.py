from django.shortcuts import render
from .models import Profile, Follow
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request=='POST':
        return render(request, 'accounts/signup.html')
    else:
        return render(request, 'accounts/signup.html')