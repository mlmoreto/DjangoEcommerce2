# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20160520_1435'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('cart', 'game')]),
        ),
    ]
