# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 19:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'ordering': ('user',), 'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'ordering': ('pedido',), 'verbose_name': 'Produto dos Pedidos', 'verbose_name_plural': 'Produtos dos Pedidos'},
        ),
    ]
