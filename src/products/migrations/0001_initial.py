# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-27 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.upload_location)),
                ('category', models.CharField(default='Others', max_length=120)),
                ('brand', models.CharField(default='Others', max_length=120)),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField(null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]