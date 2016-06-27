# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0012_auto_20160626_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tour',
            name='Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
