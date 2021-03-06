# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mods', '0003_auto_20170420_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod',
            name='descriprion',
            field=models.TextField(help_text='Полное, или доступное, описания предмета или его действия'),
        ),
        migrations.AlterField(
            model_name='mod',
            name='image',
            field=models.ImageField(upload_to='ingr/static/images/mods'),
        ),
        migrations.AlterField(
            model_name='mod',
            name='name',
            field=models.CharField(help_text='Название модификатора', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='mod',
            name='short_name',
            field=models.CharField(help_text='Короткое описание', max_length=10, unique=True),
        ),
    ]
