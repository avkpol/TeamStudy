# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0007_auto_20160626_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='priceCategory',
        ),
        migrations.AddField(
            model_name='tour',
            name='priceCategory',
            field=models.ForeignKey(default=1, to='task4_tour.PriceTourCategory'),
            preserve_default=False,
        ),
    ]
