# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20160513_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='senha',
        ),
    ]
