# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0008_coach_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
