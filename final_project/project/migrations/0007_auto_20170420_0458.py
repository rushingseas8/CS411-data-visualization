# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20170420_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.IntegerField(default=1492664283648.641, editable=False),
        ),
    ]
