# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-13 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20160513_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthDate',
            field=models.DateField(null=True),
        ),
    ]
