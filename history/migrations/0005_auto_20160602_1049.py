# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 13:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_auto_20160602_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valorUnitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
