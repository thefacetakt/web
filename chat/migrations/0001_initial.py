# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0005_remove_userprofile_likes_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Create time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_chat', to='user.UserProfile')),
                ('users', models.ManyToManyField(related_name='chat', to='user.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='user.UserProfile')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='chat.Chat')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
