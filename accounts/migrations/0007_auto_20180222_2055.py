# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-22 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180222_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='phone1',
            field=models.IntegerField(blank=True, max_length=11),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='phone2',
            field=models.IntegerField(max_length=11),
        ),
    ]
