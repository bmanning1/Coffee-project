# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0017_auto_20170430_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 30, 23, 20, 55, 715000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 30, 23, 20, 55, 715000, tzinfo=utc)),
        ),
    ]
