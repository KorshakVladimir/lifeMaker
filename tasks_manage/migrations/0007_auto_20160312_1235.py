# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_manage', '0006_auto_20160312_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_execute',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='date_plan_execute',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
