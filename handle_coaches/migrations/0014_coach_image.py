# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0013_auto_20160103_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='image',
            field=models.ImageField(default='static_files/images/None/no-img.jpg', upload_to='static_files/images'),
        ),
    ]
