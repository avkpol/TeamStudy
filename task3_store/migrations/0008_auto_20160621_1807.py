# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0007_auto_20160621_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufactureproduct',
            name='expDate',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Expire Date', null=True),
        ),
        migrations.AlterField(
            model_name='manufactureproduct',
            name='manufDate',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Manufacture Date', null=True),
        ),
    ]
