# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.ManyToManyField(to='blog.Categories'),
        ),
    ]
