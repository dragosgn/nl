# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0010_auto_20160103_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='description',
            field=models.CharField(default='Escribe aqui la descripcion del jugador.', max_length=500),
        ),
    ]
