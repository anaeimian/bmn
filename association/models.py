import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from users.models import BMNUser, Field


def association_logo_path(instance, filename):
    os.umask(0)
    path = 'associations/%s' % instance.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)


class Facility(models.Model):
    class Meta:
        verbose_name = _('Facility')
        verbose_name_plural = _('Facilities')

    title = models.CharField(
        _('Title'),
        max_length=200,
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title


class Association(models.Model):
    class Meta:
        verbose_name = _('Association')
        verbose_name_plural = _('Associations')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        verbose_name=_('BMNUser'),
    )

    fields = models.ManyToManyField(
        Field,
        related_name='associations',
        verbose_name=_('Fields'),
        null=True, blank=True,
    )

    facilities = models.ManyToManyField(
        Facility,
        related_name='associations',
        verbose_name=_('Facility'),
        null=True, blank=True,
    )

    url = models.URLField(
        verbose_name=_("Association URL"),
        null=True, blank=True
    )

    logo = models.FileField(
        null=True, blank=True,
        verbose_name=_("Association Logo"),
        upload_to=association_logo_path,
    )

    def __str__(self):
        return self.user.first_name

    def __unicode__(self):
        return u'%s' % self.user