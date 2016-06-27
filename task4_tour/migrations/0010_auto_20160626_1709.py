# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0009_auto_20160626_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetourcategory',
            old_name='highSeason',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='lastMinute',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='lowSeason',
        ),
        migrations.RemoveField(
            model_name='pricetourcategory',
            name='midSeason',
        ),
        migrations.AddField(
            model_name='pricetourcategory',
            name='season',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
