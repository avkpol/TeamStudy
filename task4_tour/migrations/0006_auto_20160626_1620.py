# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0005_auto_20160626_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='season',
        ),
        migrations.AddField(
            model_name='tour',
            name='priceCategory',
            field=models.ManyToManyField(to='task4_tour.PriceTourCategory'),
        ),
    ]
