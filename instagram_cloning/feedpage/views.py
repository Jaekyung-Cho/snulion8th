from django.shortcuts import render
from .models import Feed, Like, FeedComment
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
#from django.contrib.auth.models import User 

def home(request):
  if request.method=='POST':
    content = request.POST['content']
    photo =  request.FILES.get('photo', False) #유효성검사 통과f를 위한 False
    Feed.objects.create( content=content, author= request.user, photo=photo)
    return redirect('/home/')
  elif request.method=='GET':
    feeds = Feed.objects.all()
    return render(request, 'feedpage/home.html',{'feeds':feeds})

def new(request):
  return render(request, 'feedpage/new.html')

def delete(request, id):
  feed = Feed.objects.get(id = id)
  feed.delete()
  return redirect('/home/')

def like_feed(request, pk):
  feed = Feed.objects.get(id = pk)
  like_list = feed.like_set.filter(user_id = request.user.id)
  if like_list.count() >0:
    feed.like_set.get(user_id = request.user.id).delete()
  else:
    Like.objects.create(user_id = request.user.id, feed_id = pk)
  
  context = {
    'fid' : feed.id,
    'like_count' : like_list.count() 
  }
  return JsonResponse(context)

def new_comment(request, id):
  content = request.POST['content']
  FeedComment.objects.create(feed_id = id, content = content, author = request.user)
  comment = FeedComment.objects.latest('id')

  context = {
    'id' : comment.id,
    'username' : comment.author.username,
    'content' : comment.content
  }
  
  return JsonResponse(context)

def logout_popup(request):
  return render(request, 'feedpage/logout_popup.html')