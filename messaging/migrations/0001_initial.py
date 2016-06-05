# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('lastMessageTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Message Timestamp')),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(related_name='Conversation_reciever', verbose_name='Con Message Reciever', to=settings.AUTH_USER_MODEL)),
                ('receiver2', models.ForeignKey(related_name='Conversation_receiver2', blank=True, null=True, verbose_name='Con Message Receiver2', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='Conversation_sender', verbose_name='Con Message Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True, verbose_name='Message Text')),
                ('attachment', models.FileField(upload_to='messages/<built-in function id>', blank=True, null=True, verbose_name='Message Attachment')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Message Timestamp')),
                ('application', models.ForeignKey(blank=True, null=True, verbose_name='Message Application', to='users.Application')),
                ('conversation', models.ForeignKey(to='messaging.Conversation')),
                ('reciever', models.ForeignKey(related_name='reciever', verbose_name='Message Reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', verbose_name='Message Sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
