from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Follow
from django.shortcuts import redirect
from django.http import HttpResponse
# Create your views here.

def signup(request):
    if request.method=='POST':
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
        user.profile.college = request.POST['college']
        user.profile.major = request.POST['major']
        user.profile.birth = request.POST['birth']
        user.profile.address = request.POST['address']
        user.save()
        auth.login(request, user)
        return redirect('/home/')
    else:
        return render(request, 'accounts/signup.html')