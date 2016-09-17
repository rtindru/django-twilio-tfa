# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TFAProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authy_id', models.IntegerField(unique=True, null=True)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone_number', models.IntegerField()),
                ('country_code', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
