# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170209_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 9, 13, 16, 2, 291092, tzinfo=utc)),
        ),
    ]
