# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cons.models


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0004_auto_20160428_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='militaryapplication',
            name='postdoc_backgournd_completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='joboffers',
            name='photo_of_contract',
            field=models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Photo of Contract'),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='application',
            field=models.ForeignKey(related_name='grants', to='cons.MilitaryApplication'),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='grant_currency',
            field=models.CharField(max_length=1, verbose_name='Grant Currency', choices=[(b'0', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1'), (b'1', b'\xdb\x8c\xd9\x88\xd8\xb1\xd9\x88'), (b'2', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')]),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='photo_of_certificate',
            field=models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Grant Certificate Image'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_currency',
            field=models.CharField(max_length=1, verbose_name='Scholarship Currency', choices=[(b'0', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1'), (b'1', b'\xdb\x8c\xd9\x88\xd8\xb1\xd9\x88'), (b'2', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')]),
        ),
    ]
