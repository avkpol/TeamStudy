# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceTourCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('highSn', models.BooleanField(default=True)),
                ('middleSn', models.BooleanField(default=False)),
                ('lowSn', models.BooleanField(default=False)),
                ('lastMinute', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('tourPrice', models.DecimalField(null=True, max_digits=20, decimal_places=2, blank=True)),
                ('location', models.CharField(max_length=255)),
                ('hotel', models.CharField(max_length=255)),
                ('placePerTour', models.IntegerField(null=True, blank=True)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('Date', models.DateField(default=django.utils.timezone.now, verbose_name=b'Receive Date')),
                ('inStock', models.BooleanField(default=False)),
                ('discount', models.BooleanField(default=False)),
                ('tourPayed', models.BooleanField(default=False)),
                ('tourPartlyPayed', models.BooleanField(default=False)),
                ('highSeason', models.BooleanField(default=True)),
                ('lowSeason', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TourDirectCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=255, null=True, blank=True)),
                ('hotel', models.CharField(max_length=255, null=True, blank=True)),
                ('ski', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('address', models.CharField(max_length=250)),
                ('photo', models.ImageField(null=True, upload_to=b'img/', blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('skype', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile', models.IntegerField(null=True, blank=True)),
                ('choiceTour', models.ManyToManyField(to='task4_tour.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='TransTourCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('busTour', models.BooleanField(default=False)),
                ('autoTour', models.BooleanField(default=False)),
                ('airTour', models.BooleanField(default=True)),
                ('seaTour', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='directCategory',
            field=models.ForeignKey(to='task4_tour.TourDirectCategory'),
        ),
        migrations.AddField(
            model_name='tour',
            name='priceCategory',
            field=models.ForeignKey(to='task4_tour.PriceTourCategory'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tourists',
            field=models.ManyToManyField(to='task4_tour.Tourist'),
        ),
        migrations.AddField(
            model_name='tour',
            name='transCategory',
            field=models.ForeignKey(to='task4_tour.TransTourCategory'),
        ),
    ]
