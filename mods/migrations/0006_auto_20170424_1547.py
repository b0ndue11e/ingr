# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 12:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0005_auto_20170424_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod',
            name='instruction',
        ),
        migrations.RemoveField(
            model_name='mod',
            name='practice',
        ),
    ]
