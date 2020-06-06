# Generated by Django 3.0.5 on 2020-06-06 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedpage', '0005_auto_20200531_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
