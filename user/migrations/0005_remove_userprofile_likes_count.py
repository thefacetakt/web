# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 03:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_userprofile_likes_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_count',
        ),
    ]