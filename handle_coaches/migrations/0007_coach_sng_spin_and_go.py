# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0006_auto_20151230_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='sng_spin_and_go',
            field=models.BooleanField(default=False, verbose_name='SNG Spin And Go'),
        ),
    ]