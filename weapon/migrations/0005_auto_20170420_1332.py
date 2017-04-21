# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapon', '0004_auto_20170420_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='posititon',
            field=models.CharField(choices=[('W', 'Weapon'), ('V', 'Virus')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='name',
            field=models.CharField(help_text='Название оружия', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='type',
            field=models.CharField(choices=[('W', 'Weapon'), ('V', 'Virus')], default='Weapon', help_text='Выберите тип оружия Разрущающее или Захватывающее', max_length=6),
        ),
    ]