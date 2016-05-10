# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0007_memberships_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberships',
            name='title_of_association',
            field=models.CharField(max_length=300, verbose_name='Membership Association Title'),
        ),
    ]
