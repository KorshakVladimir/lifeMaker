# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manage', '0007_auto_20160312_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
