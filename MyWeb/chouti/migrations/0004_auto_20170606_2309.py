# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-06 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chouti', '0003_auto_20170606_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenews',
            name='publisher',
        ),
        migrations.AlterField(
            model_name='imagenews',
            name='desc',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
