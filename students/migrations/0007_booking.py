# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-01 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20190501_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('s1', models.IntegerField(default=0)),
                ('s2', models.IntegerField(default=0)),
                ('s3', models.IntegerField(default=0)),
                ('s4', models.IntegerField(default=0)),
            ],
        ),
    ]