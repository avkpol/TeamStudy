# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0008_auto_20160626_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='priceCategory',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='priceCategory',
        ),
        migrations.RemoveField(
            model_name='tourdirectcategory',
            name='ski',
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='highSeason',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='lastMinute',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='lowSeason',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='midSeason',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='tourdirectcategory',
            name='price',
            field=models.ForeignKey(default=1, to='task4_tour.PriceTourCategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tour',
            name='tourPrice',
            field=models.ForeignKey(default=1, to='task4_tour.PriceTourCategory'),
            preserve_default=False,
        ),
    ]
