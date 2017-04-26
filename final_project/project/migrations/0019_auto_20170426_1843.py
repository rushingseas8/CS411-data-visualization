# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-26 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_auto_20170426_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(default=uuid.uuid4, editable=False, max_length=200, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='data',
            name='create_time',
            field=models.IntegerField(default=1493232223829.397),
        ),
        migrations.AlterField(
            model_name='data',
            name='upload_time',
            field=models.IntegerField(default=1493232223829.374, editable=False),
        ),
    ]
