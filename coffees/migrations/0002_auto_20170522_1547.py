# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import coffees.models


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=coffees.models.get_subscription_end_date),
        ),
    ]
