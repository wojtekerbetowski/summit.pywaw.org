# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20150321_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='company_address',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='company_name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='company_nip',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='invoice',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='twitter',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
