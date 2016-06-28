# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0002_auto_20160628_0426'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mark', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='driver',
            name='auto',
            field=models.ManyToManyField(to='task4_taxi.Auto'),
        ),
    ]
