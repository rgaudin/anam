# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_on', models.DateTimeField(auto_now_add=True)),
                ('dataset', jsonfield.fields.JSONField(blank=True, default=[])),
            ],
        ),
    ]
