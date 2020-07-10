from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile, Follow
from django.shortcuts import redirect
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate as django_authenticate
from django.http import HttpResponse, JsonResponse
# Create your views here.

def signup(request):
    if request.method=='POST' and request.POST['password1']==request.POST['password2']:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
        user.profile.college = request.POST['college']
        user.profile.major = request.POST['major']
        #user.profile.birth = request.POST['birth']
        #user.profile.address = request.POST['address']
        user.save()

        login_user = django_authenticate(username=request.POST['username'],password=request.POST['password1'])
        django_login(request, login_user)
        return redirect('/home/')
    else:
        return render(request, 'accounts/signup.html')