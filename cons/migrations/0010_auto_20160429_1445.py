# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0009_editorsmembership_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorsmembership',
            name='position',
            field=models.CharField(max_length=300, verbose_name='Position'),
        ),
    ]
