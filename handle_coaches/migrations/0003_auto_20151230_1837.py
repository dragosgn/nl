# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0002_auto_20151230_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='nl_cap',
            new_name='nl_cap_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='nl_deep_stack',
            new_name='nl_deep_stack_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='nl_heads_up',
            new_name='nl_heads_up_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='nl_multistack',
            new_name='nl_multistack_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='plo_deepstack',
            new_name='plo_deepstack_FR',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='plo_hu',
            new_name='plo_hu_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='plo_multistack',
            new_name='plo_multistack_6max',
        ),
        migrations.AddField(
            model_name='coach',
            name='nl_cap_FR',
            field=models.BooleanField(default=False, verbose_name='NL CAP'),
        ),
        migrations.AddField(
            model_name='coach',
            name='nl_deep_stack_FR',
            field=models.BooleanField(default=False, verbose_name='NL DeepStack'),
        ),
        migrations.AddField(
            model_name='coach',
            name='nl_heads_up_FR',
            field=models.BooleanField(default=False, verbose_name='NL Heads Up'),
        ),
        migrations.AddField(
            model_name='coach',
            name='nl_multistack_FR',
            field=models.BooleanField(default=False, verbose_name='NL MultiStack'),
        ),
        migrations.AddField(
            model_name='coach',
            name='plo_deepstack_6max',
            field=models.BooleanField(default=False, verbose_name='PLO Deepstack'),
        ),
        migrations.AddField(
            model_name='coach',
            name='plo_hu_FR',
            field=models.BooleanField(default=False, verbose_name='PLO HU'),
        ),
        migrations.AddField(
            model_name='coach',
            name='plo_multistack_FR',
            field=models.BooleanField(default=False, verbose_name='PLO MultiStack'),
        ),
    ]
