# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0003_auto_20160620_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproduct',
            name='slug',
            field=models.SlugField(null=True, blank=True),
        ),
    ]
