# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='ads', max_length=100),
            preserve_default=False,
        ),
    ]
