# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_auto_20170420_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='user',
        ),
        migrations.AlterField(
            model_name='data',
            name='time',
            field=models.IntegerField(default=1492677603371.257, editable=False),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
