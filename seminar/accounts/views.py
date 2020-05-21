from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
	if request.method  == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
			user.profile.college = request.POST['college']
			user.profile.major = request.POST['major']
			user.profile.birth = request.POST['birth']
			user.profile.instagram = request.POST['instagram']
			user.profile.address = request.POST['address']
			user.save()
			auth.login(request, user)
			return redirect('/feeds/')
	return render(request, 'accounts/signup.html')

def update_user(request):
	if request.method == 'GET':
		user_id = request.GET.get('user')
		user = User.objects.get(id=user_id)
		return render(request, 'accounts/update_user.html', {'user':user})
	elif request.method == 'POST':
		user = User.objects.get(id=request.POST['id'])
		user.profile.college = request.POST['college']
		user.profile.major = request.POST['major']
		user.profile.birth = request.POST['birth']
		user.profile.instagram = request.POST['instagram']	
		user.profile.address = request.POST['address']
		user.save()
		return redirect('/feeds/')