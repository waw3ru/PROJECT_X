# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-13 17:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0012_auto_20180813_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='publication_date',
        ),
        migrations.RemoveField(
            model_name='evidence',
            name='slug',
        ),
    ]
