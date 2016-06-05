# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='receiver2',
            field=models.ForeignKey(related_name='Conversation_receiver2', verbose_name='Conversation Message Receiver2', null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
