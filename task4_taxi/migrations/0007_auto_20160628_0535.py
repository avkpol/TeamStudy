# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0006_auto_20160628_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='cltorder',
            name='discont_price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='cltorder',
            name='discount',
            field=models.BooleanField(default=False),
        ),
    ]
