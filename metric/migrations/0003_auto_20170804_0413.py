# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 02:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metric', '0002_auto_20170804_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='public',
            field=models.BooleanField(default=True, help_text='Select to publish metric for everyone on-line.', verbose_name='Public?'),
        ),
        migrations.AlterField(
            model_name='value',
            name='time',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
