# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 04:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20160929_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='item_type',
            new_name='content_type',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='item_id',
            new_name='object_id',
        ),
    ]