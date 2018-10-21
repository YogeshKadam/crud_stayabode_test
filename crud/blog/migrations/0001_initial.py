# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-23 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('tag', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=120)),
            ],
        ),
    ]
