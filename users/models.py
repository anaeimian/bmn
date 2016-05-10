from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from common.choices import GENDER_CHOICES, MILITARY_CHOICES, EDUCATION_CHOICES, UNIVERSITIES, COUNTRIES


class Field(models.Model):
    class Meta:
        verbose_name = _('Field')
        verbose_name_plural = _('Fields')

    title = models.CharField(
        _('Title'),
        max_length=200,
    )

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title


class BMNUser(models.Model):
    class Meta:
        verbose_name = _("BMN User")
        verbose_name_plural = _("BMN Users")

    user = models.OneToOneField(User)
    birth_country = models.CharField(
        max_length=2,
        choices=COUNTRIES,
        verbose_name=_('Birth Country'),
    )

    residence_country = models.CharField(
        max_length=2,
        choices=COUNTRIES,
        verbose_name=_('Residence Country'),
    )

    nationalID = models.CharField(
        verbose_name=_('National ID/Passport Number'),
        max_length=100
    )

    gender = models.CharField(
        verbose_name=_('Gender'),
        max_length=1,
        choices=GENDER_CHOICES
    )

    birth_date = models.DateTimeField(
        verbose_name=_('Birth Date'),
    )

    military_status = models.CharField(
        verbose_name=_('Military Status'),
        max_length=1,
        choices=MILITARY_CHOICES
    )

    education = models.CharField(
        verbose_name=_('Education'),
        max_length=1,
        choices=EDUCATION_CHOICES
    )

    university = models.CharField(
        max_length=4,
        choices=UNIVERSITIES,
        verbose_name=_('University')
    )

    phone = models.CharField(
        max_length=20,
        verbose_name=_('Phone Number'),
        null=True,
        blank=True,
    )

    mobile = models.CharField(
        max_length=20,
        verbose_name=_('Mobile Phone'),
        null=True,
        blank=True,
    )

    field = models.ForeignKey(
        Field,
        verbose_name=_('Field'),
    )

    resume = models.FileField(
        verbose_name=_('Resume'),
        upload_to=('users/' + id.__str__() + '/'),
        null=True, blank=True,
    )

    profile_picture = models.FileField(
        verbose_name=_('Profile Picture'),
        upload_to=('users/' + id.__str__() + '/'),
        null=True, blank=True
    )

    additional_info = models.TextField(
        verbose_name=_('Additional Info'),
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Application(models.Model):
    user = models.ForeignKey(
        BMNUser,
        verbose_name=_('User'),
        related_name='coop_pplications',
    )
    is_finalized = models.BooleanField(
        verbose_name=_('Finalized'),
        default=False
    )
    finalization_date = models.DateTimeField(
        verbose_name=_('Finalization Date'),
        null=True,
        blank=True,
    )