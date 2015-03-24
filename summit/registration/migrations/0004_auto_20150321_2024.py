# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_attendee_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='hash',
            field=models.CharField(max_length=32, default=registration.models.create_attendee_hash),
            preserve_default=True,
        ),
    ]
