# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0022_auto_20160621_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproduct',
            name='producer',
            field=models.ForeignKey(default=1994, to='task3_store.Manufacturer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storeproduct',
            name='receiveDate',
            field=models.DateField(default=datetime.date, verbose_name=b'Receive Date'),
        ),
    ]
