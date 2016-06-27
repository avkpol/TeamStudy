# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0004_remove_tour_tourists'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricetourcategory',
            old_name='tourSeason',
            new_name='priceCategory',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='directCategory',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='transCategory',
        ),
    ]
