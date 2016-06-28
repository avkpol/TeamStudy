# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0004_auto_20160628_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='number',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
