# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0011_auto_20160103_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='discounted',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coach',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
