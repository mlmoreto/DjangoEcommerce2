# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_auto_20160523_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.IntegerField(default=0),
        ),
    ]
