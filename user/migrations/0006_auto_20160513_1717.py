# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20160513_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cpf',
            field=models.CharField(max_length=15),
        ),
    ]
