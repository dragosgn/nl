# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 20:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0012_auto_20160104_1504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='sng_hu_hyperturbo',
            new_name='sng_hyperturbo_hu',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='sng_hu_normal',
            new_name='sng_normal_hu',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='sng_hu_turbo',
            new_name='sng_turbo_hu',
        ),
    ]
