# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-04 11:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applet', '0004_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Urls',
        ),
    ]
