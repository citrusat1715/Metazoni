# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-08 21:06
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetailsc', '0004_auto_20180509_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bookdetailsc.Category'),
        ),
    ]
