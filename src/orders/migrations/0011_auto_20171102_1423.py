# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-02 14:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20171102_0123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-id']},
        ),
    ]
