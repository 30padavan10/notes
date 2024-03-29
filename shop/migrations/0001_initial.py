# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-08-20 07:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('sale', models.BooleanField()),
                ('pub_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('good_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Good')),
                ('version_os', models.CharField(max_length=50)),
                ('display', models.CharField(max_length=50)),
                ('CPU', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
                ('GPU', models.CharField(max_length=50)),
                ('HDD', models.CharField(max_length=50)),
            ],
            bases=('shop.good',),
        ),
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('good_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shop.Good')),
                ('year', models.IntegerField()),
                ('version_os', models.CharField(max_length=50)),
                ('num_core', models.IntegerField()),
                ('frequency_cpu', models.CharField(max_length=50)),
                ('memory', models.CharField(max_length=50)),
            ],
            bases=('shop.good',),
        ),
        migrations.AddField(
            model_name='good',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Comment'),
        ),
        migrations.AddField(
            model_name='good',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Producer'),
        ),
    ]
