# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-02 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20171130_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colname', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
    ]
