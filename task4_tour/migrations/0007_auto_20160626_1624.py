# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0006_auto_20160626_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricetourcategory',
            name='priceCategory',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
