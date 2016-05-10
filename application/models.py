# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.db import models
from django.utils import timezone

from users.models import Application, Field
from association.models import Association, Facility
from django.utils.translation import ugettext as _


def coopertaion_attachment_path(instance, filename):
    print("Filename: " + filename)
    os.umask(0)
    path = 'applications/cooperation/%s/' % instance.application.application.user.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)


class CoopApplication(models.Model):
    class Meta:
        verbose_name = _('Cooperation Application')
        verbose_name_plural = _('Cooperation Applications')

    application = models.OneToOneField(
        Application,
        related_name="coop_app",
    )
    facility = models.ForeignKey(
        Facility,
        related_name="coop_applications",
        verbose_name=_('Facility'),
    )

    manager_has_verified = models.BooleanField(
        default=False,
        verbose_name=_('First verify'),
    )
    association_has_verified = models.BooleanField(
        default=False,
        verbose_name=_('Association verify'),
    )
    manager_verification_date = models.DateTimeField(
        null=True,
        blank=True,
        default=timezone.now,
    )
    field = models.ForeignKey(
        Field,
        verbose_name=_("Application Field"),
        related_name='coop_applications'
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Is deleted")
    )
    status = models.CharField(
        max_length=1,
        verbose_name=_("Status"),
        choices=(
            ('0', 'ثبت نهایی نشده'),
            ('1', 'بررسی نشده'),
            ('2', 'در حال بررسی'),
            ('3', 'در حال مذاکره'),
            ('4', 'عقد قرارداد'),
            ('5', 'شروع همکاری'),
            ('6', 'قطع همکاری'),
            ('7', 'اتمام همکاری'),
            ('8', 'رد شده'),
        ),
        default='1',
    )

    def __unicode__(self):
        return u'%s - %s - %s - %s' % (self.facility, self.field, self.user, self.id)


class Association_Application(models.Model):
    association = models.ForeignKey(Association)
    application = models.ForeignKey(CoopApplication)
    priority = models.CharField(max_length=2,
                                choices=(('1', 'الویت اول'),
                                         ('2', 'الویت دوم'),
                                         ('3', 'الویت سوم'),
                                         )
                                )


class TextExtraAttachment(models.Model):
    application = models.ForeignKey(
        CoopApplication,
        related_name='text_extra_attachments'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Requirement Title'
    )
    text = models.TextField(
        verbose_name=_('Text Extra Attachment'),
        null=True, blank=True
    )


class FileExtraAttachment(models.Model):
    application = models.ForeignKey(
        CoopApplication,
        related_name='file_extra_attachments'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Requirement Title'
    )
    file = models.FileField(
        upload_to=coopertaion_attachment_path,
        null=True, blank=True,
        verbose_name=_("File Extra Attachment")
    )


class Review(models.Model):
    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    application = models.OneToOneField(
        CoopApplication
    )
    note = models.TextField(
        verbose_name=_('Notes'),
        null=True,
        blank=True
    )
    made_decision_date = models.DateTimeField(
        _('Made decision date'),
        null=True,
        blank=True,
    )
    decision = models.BooleanField(
        default=False,
        verbose_name=_('Association decision'),
    )

    def __unicode__(self):
        return u'%s' % self.id


class RequirementField(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Requirement Title',
    )
    facility = models.ForeignKey(
        Facility,
        verbose_name=_('Requirement Facility'),
        related_name='facility_requirements'
    )
    type = models.CharField(max_length=1,
                            choices=(
                                ('0', 'Text'),
                                ('1', 'File'),
                            )
                            )

    def __str__(self):
        return self.get_type_display() + ": " + self.title
