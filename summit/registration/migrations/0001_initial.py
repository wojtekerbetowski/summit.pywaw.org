# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('twitter', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('display_on_website', models.BooleanField(default=True)),
                ('notes', models.TextField()),
                ('invoice', models.BooleanField(default=False)),
                ('company_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=500)),
                ('company_nip', models.CharField(max_length=10)),
                ('is_paid', models.BooleanField(default=False)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
