# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffees', '0003_purchase_subscription_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='subscription_end',
            new_name='subscription_created_date',
        ),
    ]
