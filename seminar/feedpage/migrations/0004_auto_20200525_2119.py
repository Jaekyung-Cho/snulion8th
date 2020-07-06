# Generated by Django 3.0.5 on 2020-05-25 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedpage', '0003_auto_20200523_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedcomment',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_feedcomments', through='feedpage.Like', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='like',
            name='feedcomment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feedpage.FeedComment'),
        ),
    ]