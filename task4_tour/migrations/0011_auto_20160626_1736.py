# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0010_auto_20160626_1709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='placePerTour',
        ),
        migrations.RemoveField(
            model_name='transtourcategory',
            name='airTour',
        ),
        migrations.RemoveField(
            model_name='transtourcategory',
            name='autoTour',
        ),
        migrations.RemoveField(
            model_name='transtourcategory',
            name='busTour',
        ),
        migrations.RemoveField(
            model_name='transtourcategory',
            name='seaTour',
        ),
        migrations.AddField(
            model_name='tour',
            name='tourOrdered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tour',
            name='tourTransfer',
            field=models.ForeignKey(default=1, to='task4_tour.TransTourCategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transtourcategory',
            name='price',
            field=models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='transtourcategory',
            name='transfer',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
