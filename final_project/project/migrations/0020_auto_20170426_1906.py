# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0019_auto_20170426_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='create_time',
            field=models.IntegerField(default=1493233585090.676),
        ),
        migrations.AlterField(
            model_name='data',
            name='upload_time',
            field=models.IntegerField(default=1493233585090.652, editable=False),
        ),
    ]