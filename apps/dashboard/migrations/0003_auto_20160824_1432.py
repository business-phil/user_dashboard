# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160823_2007'),
        ('dashboard', '0002_auto_20160824_1357'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='messageuser',
        ),
        migrations.AddField(
            model_name='message',
            name='walluser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='userwall', to='login.User'),
            preserve_default=False,
        ),
    ]