# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='priceCategory',
            new_name='season',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='highSeason',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='lowSeason',
        ),
    ]
