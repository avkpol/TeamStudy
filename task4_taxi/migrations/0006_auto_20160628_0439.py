# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0005_auto_20160628_0437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='fulf_order',
        ),
        migrations.AddField(
            model_name='driver',
            name='fulf_order',
            field=models.ManyToManyField(to='task4_taxi.CltOrder'),
        ),
    ]
