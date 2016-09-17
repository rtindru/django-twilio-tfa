# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfa_demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='uid',
            field=models.IntegerField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
