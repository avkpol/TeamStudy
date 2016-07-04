# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0017_auto_20160621_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeproduct',
            name='producer',
            field=models.ForeignKey(default=1, to='task3_store.Manufacturer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='storeproduct',
            name='image',
            field=models.ImageField(null=True, upload_to=b'img/', blank=True),
        ),
        migrations.AlterField(
            model_name='storeproduct',
            name='receiveDate',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Receive Date'),
        ),
    ]
