from django.db import models
from faker import Faker
from django.contrib.auth.models import User  
from django.utils import timezone

# Create your models here.
class Feed(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    like_users = models.ManyToManyField(User, through="Like", related_name="like_feeds", blank=True)
    photo = models.ImageField(blank = True, upload_to='feed_photos')

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['created_at']

    def update_date(self): # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    like_count = models.IntegerField(default = 0)



