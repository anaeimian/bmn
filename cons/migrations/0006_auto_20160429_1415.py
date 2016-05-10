# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cons.models


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0005_auto_20160429_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='militaryapplication',
            name='editors_memberships_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='militaryapplication',
            name='memberships_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postdocbackground',
            name='photo_of_document',
            field=models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Photo of Postdoc Document'),
        ),
    ]
