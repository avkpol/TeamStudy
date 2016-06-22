# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0023_auto_20160622_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='receiveDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Receive Date'),
        ),
    ]
