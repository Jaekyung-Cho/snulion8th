# Generated by Django 3.0.5 on 2020-05-25 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedpage', '0008_auto_20200525_2252'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedcomment',
            options={'ordering': ['-like_count', 'create_at']},
        ),
    ]
