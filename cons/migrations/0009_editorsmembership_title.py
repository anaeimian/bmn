# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0008_auto_20160429_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorsmembership',
            name='title',
            field=models.CharField(default='Empty', max_length=300, verbose_name='Journal Title'),
            preserve_default=False,
        ),
    ]
