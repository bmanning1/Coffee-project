# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0019_auto_20170426_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 30, 12, 25, 9, 610000, tzinfo=utc)),
        ),
    ]
