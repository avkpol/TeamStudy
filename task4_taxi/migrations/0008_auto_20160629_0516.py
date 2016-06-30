# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task4_taxi', '0007_auto_20160628_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cltorder',
            name='destination',
            field=models.CharField(max_length=100, choices=[(b'Poltava', b'Poltava'), (b'Lubny', b'Lubny'), (b'Gorbanivka', b'Gorbanivka')]),
        ),
    ]
