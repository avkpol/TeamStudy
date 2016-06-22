# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0009_auto_20160621_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufactureproduct',
            name='expDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Expire Date'),
        ),
        migrations.AlterField(
            model_name='manufactureproduct',
            name='manufDate',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'Manufacture Date'),
        ),
    ]
