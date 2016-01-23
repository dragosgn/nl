# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-04 22:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('handle_coaches', '0018_remove_coach_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_cap_6max',
            new_name='nl_cap_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_cap_FR',
            new_name='nl_cap_FR',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_deep_stack_6max',
            new_name='nl_deep_stack_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_deep_stack_FR',
            new_name='nl_deep_stack_FR',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_multistack_6max',
            new_name='nl_multistack_6max',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='cash_nl_multistack_FR',
            new_name='nl_multistack_FR',
        ),
    ]
