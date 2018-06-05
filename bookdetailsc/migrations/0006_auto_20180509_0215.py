# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-08 21:15
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bookdetailsc', '0005_auto_20180509_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='bookdetailsc.Category'),
        ),
    ]
