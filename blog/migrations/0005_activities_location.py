# Generated by Django 2.0.7 on 2019-07-25 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190725_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='activities',
            name='location',
            field=models.CharField(default="This event hasn't set a location", max_length=200),
        ),
    ]
