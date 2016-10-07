# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-06 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kegiatan', models.CharField(max_length=120)),
                ('waktu', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
