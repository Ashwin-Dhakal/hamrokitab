# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_auto_20171205_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Edition',
            field=models.CharField(choices=[('first', 'first'), ('second', 'second'), ('third', 'third'), ('forth', 'forth'), ('fifth', 'fifth'), ('sixth', 'sixth'), ('seventh', 'seventh'), ('eighth', 'eighth'), ('ninth', 'ninth'), ('tenth', 'tenth')], default='first', max_length=10),
        ),
    ]
