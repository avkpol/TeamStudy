# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='fulfOrder',
            new_name='fulf_order',
        ),
        migrations.RenameField(
            model_name='driver',
            old_name='name',
            new_name='last_name',
        ),
    ]
