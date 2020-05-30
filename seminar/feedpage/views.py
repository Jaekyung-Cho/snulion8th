from django.shortcuts import render
from .models import Feed, FeedComment, Like
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 

# Create your views here.

def index(request):
  if request.method == 'GET':
    feeds = Feed.objects.all()
    return render(request, 'feedpage/index.html',{'feeds':feeds})

  elif request.method =='POST':
    title = request.POST['title']
    content = request.POST['content']
    photo =  request.FILES.get('photo', False) #유효성검사 통과를 위한 False
    Feed.objects.create(title=title, content=content, author= request.user, photo=photo)
    return redirect('/feeds/')


def new(request):
  return render(request, 'feedpage/new.html')

def show(request, id):
  feed = Feed.objects.get(id = id)
  if request.method=='GET':
    return render(request, 'feedpage/show.html',{'feed':feed})

  elif request.method == 'POST':
    feed.title=request.POST['title']
    feed.content=request.POST['content']
    feed.save()

    redirect_to = request.GET.get('next')
    return redirect(redirect_to)

def delete(request, id):
  feed = Feed.objects.get(id = id)
  feed.delete()
  return redirect('/feeds/')

def update(request, id):
  feed = Feed.objects.get(id = id )
  redirect_to = request.GET.get('next')
  return render(request,'feedpage/update.html',{'feed':feed,'redirect_to':redirect_to})

def delete_comment(request, id, cid):
  c = FeedComment.objects.get(id = cid)
  c.delete()
  return redirect('/feeds/')

def create_comment(request, id):
  content = request.POST['content']
  FeedComment.objects.create(feed_id=id, content=content, author=request.user)
  return redirect('/feeds/')

def feed_like(request, pk):
  feed = Feed.objects.get(id=pk)
  like_list = feed.like_set.filter(user_id = request.user.id)
  if like_list.count() > 0:
    feed.like_set.get(user_id = request.user.id).delete()
  else:
    Like.objects.create(user_id = request.user.id, feed_id = feed.id)
  
  return redirect('/feeds/')

def feedcomment_like(request, pk):
  feedcomment = FeedComment.objects.get(id = pk)
  like_list = feedcomment.like_set.filter(user_id = request.user.id)
  if like_list.count() >0:
    feedcomment.like_count -= 1
    feedcomment.save()
    feedcomment.like_set.get(user_id = request.user.id).delete()
  else:
    feedcomment.like_count += 1
    feedcomment.save()
    Like.objects.create(user_id = request.user.id, feedcomment_id = feedcomment.id)

  return redirect('/feeds/')