# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0002_auto_20170522_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='subscription_valid',
            field=models.BooleanField(default=True),
        ),
    ]
