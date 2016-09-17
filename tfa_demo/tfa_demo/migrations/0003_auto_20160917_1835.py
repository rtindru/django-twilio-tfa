# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tfa_demo', '0002_auto_20160917_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='phone_number',
            new_name='phone',
        ),
    ]
