import os
from django import utils
from django.conf import settings
from django.db import models


def notice_attachment_path(instance, filename):
    os.umask(0)
    path = 'notices/%s' % instance.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)

    return os.path.join(path, filename.replace(',', '').replace(' ', ''))


def news_attachment_path(instance, filename):
    os.umask(0)
    path = 'news/%s' % instance.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)

    return os.path.join(path, filename.replace(',', '').replace(' ', ''))


class Question(models.Model):
    question_text = models.TextField(
        verbose_name='FAQ Question Text'
    )
    answer_text = models.TextField(
        verbose_name='FAQ Answer Text'
    )


class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='News Title',
        null=True, blank=True
    )
    news_text = models.TextField(
        verbose_name='News Text'
    )
    creation_date = models.DateTimeField(
        verbose_name='News Creation Date',
        default=utils.timezone.now,
    )
    attachment = models.FileField(
        verbose_name='News Attachment',
        null=True, blank=True,
        upload_to=news_attachment_path,
    )

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Notice Title',
        null=True, blank=True
    )
    notice_text = models.TextField(
        verbose_name='Notice Text'
    )
    initiation_date = models.DateTimeField(
        verbose_name='Notice Creation Date',
        default=utils.timezone.now,
    )
    expiration_date = models.DateTimeField(
        verbose_name='Notice Expiration Date',
        null=True, blank=True
    )
    attachment = models.FileField(
        verbose_name='Notice Attachment',
        null=True, blank=True,
        upload_to=notice_attachment_path,
    )

    def __str__(self):
        return self.title
