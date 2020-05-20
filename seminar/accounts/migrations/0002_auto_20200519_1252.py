# Generated by Django 3.0.5 on 2020-05-19 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]