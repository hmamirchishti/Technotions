# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-12 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='u',
            new_name='user',
        ),
    ]
