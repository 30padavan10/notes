# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-08 05:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title', max_length=200)),
                ('body', models.TextField(help_text='description', max_length=20000)),
                ('pub_date', models.DateField()),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
