# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_friendship'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='isCommunity',
            field=models.BooleanField(default=False),
        ),
    ]
