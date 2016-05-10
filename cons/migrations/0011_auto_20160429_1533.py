# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0010_auto_20160429_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='application',
            field=models.OneToOneField(to='cons.MilitaryApplication'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
