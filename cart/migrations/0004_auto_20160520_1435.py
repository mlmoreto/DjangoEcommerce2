# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 17:35
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20160520_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='quantidade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
