# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-22 15:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180222_2026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='shipping_address_1',
            new_name='shippingAddress_1',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='shipping_address_2',
            new_name='shippingAddress_2',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='shipping_city',
            new_name='shippingCity',
        ),
        migrations.RenameField(
            model_name='useraddress',
            old_name='shipping_state',
            new_name='shippingState',
        ),
    ]
