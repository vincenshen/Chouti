# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-06 10:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chouti', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='article',
            new_name='new',
        ),
        migrations.AlterField(
            model_name='news',
            name='href',
            field=models.URLField(default='', max_length=100),
        ),
    ]
