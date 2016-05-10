# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0006_auto_20160429_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='memberships',
            name='length',
            field=models.IntegerField(default=0, verbose_name='Membership length'),
            preserve_default=False,
        ),
    ]
