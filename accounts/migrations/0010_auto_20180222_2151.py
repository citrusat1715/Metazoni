# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-22 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180222_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='firstName',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='lastName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
