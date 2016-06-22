# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task3_store', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Agents',
            new_name='Agent',
        ),
        migrations.RenameModel(
            old_name='Distributors',
            new_name='Distributor',
        ),
        migrations.RenameModel(
            old_name='Manufacturers',
            new_name='Manufacturer',
        ),
    ]
