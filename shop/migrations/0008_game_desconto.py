# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 21:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20160518_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
