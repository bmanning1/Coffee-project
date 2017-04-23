# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=254)),
                ('description', models.TextField()),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscription_end', models.DateTimeField(default=datetime.datetime(2017, 1, 20, 22, 45, 41, 661378, tzinfo=utc))),
                ('coffee', models.ForeignKey(to='coffees.Coffee')),
                ('user', models.ForeignKey(related_name='purchases', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
