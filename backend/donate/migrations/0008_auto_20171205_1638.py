# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-05 10:53
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0007_auto_20171205_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Class',
            field=models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='details',
            name='Ward_number',
            field=models.PositiveSmallIntegerField(default='1'),
        ),
    ]
