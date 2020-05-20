from django.db import models
from django.utils import timezone
from faker import Faker
from django.contrib.auth.models import User 

from django.db.models.signals import post_save  # 추가
from django.dispatch import receiver   # 추가


#User 와 1대1로 대응되는 관계
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 하나 지우면 같이 지워지도록
    college = models.CharField(max_length=20, blank=True)  #
    major = models.CharField(max_length=20, blank=True)
    birth = models.DateField(auto_now=False, auto_now_add=False, default="2020-01-01")
    instagram = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    


    def __str__(self):   # 추가
        return 'id=%d, user_id=%d, college=%s, major=%s, birth=%s, instagram=%s, address=%s' % (self.id, self.user.id, self.college, self.major, self.birth, self.instagram, self.address)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):  
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):  
        instance.profile.save()
# Create your models here.
