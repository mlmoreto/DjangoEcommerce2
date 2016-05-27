# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 19:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0008_game_desconto'),
        ('user', '0018_auto_20160515_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=100, validators=[django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(validators=django.core.validators.MaxValueValidator(1))),
                ('valorUnitario', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.1)])),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Game')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='history.Pedido')),
            ],
        ),
    ]