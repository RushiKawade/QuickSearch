# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-04 11:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applet', '0002_auto_20190404_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='urls',
            old_name='id',
            new_name='Id',
        ),
    ]
