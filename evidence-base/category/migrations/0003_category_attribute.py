# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-23 03:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attribute', '0002_attribute_board'),
        ('category', '0002_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='attribute.Attribute'),
        ),
    ]