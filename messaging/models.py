from django import utils
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from users.models import Application


class Message(models.Model):
    text = models.TextField(
        verbose_name=_('Message Text'),
        null=True,
        blank=True,
    )

    sender = models.ForeignKey(
        User,
        verbose_name=_('Message Sender'),
        related_name='sender'
    )
    reciever = models.ForeignKey(
        User,
        verbose_name=_('Message Reciever'),
        related_name='reciever'
    )
    application = models.ForeignKey(
        Application,
        null=True,
        blank=True,
        verbose_name=_('Message Application')
    )
    attachment = models.FileField(
        null=True,
        blank=True,
        verbose_name=_('Message Attachment'),
        upload_to=('messages/' + id.__str__())
    )
    timestamp = models.DateTimeField(
        verbose_name='Message Timestamp',
        default=utils.timezone.now,
    )
    is_read = models.BooleanField(
        default=False,
    )
