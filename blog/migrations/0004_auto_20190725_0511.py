# Generated by Django 2.0.7 on 2019-07-25 05:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_activity'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Activity',
            new_name='Activities',
        ),
    ]
