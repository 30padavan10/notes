# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-20 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_good_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.CharField(blank=True, choices=[('s', 'Смартфон'), ('n', 'Ноутбук')], default='s', max_length=1),
        ),
    ]