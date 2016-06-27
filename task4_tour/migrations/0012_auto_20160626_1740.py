# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_tour', '0011_auto_20160626_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transtourcategory',
            old_name='transfer',
            new_name='transportation',
        ),
    ]
