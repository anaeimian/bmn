# -*- coding: utf-8 -*-

import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from users.models import Application
from common.choices import INTERNAL_JOURNALS, UNIVERSITIES_ALL, COUNTRIES, UNIVERSITIES, SC_ISI_JOURNALS


def military_attachment_path_with_user(instance, filename):
    os.umask(0)
    path = 'applications/military/%s' % instance.application.user.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)


def military_attachment_path(instance, filename):
    os.umask(0)
    path = 'applications/military/%s' % instance.application.user.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)


def military_side_attachment_path(instance, filename):
    os.umask(0)
    path = 'applications/military/%s' % instance.application.application.user.id
    att_path = os.path.join(settings.MEDIA_ROOT, path)
    if settings.DEFAULT_FILE_STORAGE == "django.core.files.storage.FileSystemStorage":
        if not os.path.exists(att_path):
            os.makedirs(att_path, 0o777)
    return os.path.join(path, filename)


class MilitaryApplication(models.Model):
    application = models.OneToOneField(
        Application,
        related_name='military_app',
    )
    personneli_photo = models.FileField(
        verbose_name=_('Personneli Photo'),
        upload_to=military_attachment_path_with_user,
    )
    national_id_photo = models.FileField(
        verbose_name=_('National ID Photo'),
        upload_to=military_attachment_path_with_user,
    )
    social_id_number = models.CharField(
        verbose_name=_('Social ID Number'),
        max_length=10,
    )
    marital_status = models.CharField(
        max_length=1, choices=(
            ('0', 'مجرد'),
            ('1', 'متاهل'),
        ),
        verbose_name=_('Marital Status')
    )
    national_booklet_photo = models.FileField(
        verbose_name=_('First Page of National Booklet Photo'),
        upload_to=military_attachment_path_with_user,
    )
    inner_phone_number = models.CharField(
        verbose_name=_('Phone Number Inside Country'),
        max_length=20
    )
    outer_phone_number = models.CharField(
        verbose_name=_('Phone Number Outside Country'),
        max_length=20,
        null=True, blank=True
    )
    in_country_period_start = models.DateField(
        verbose_name=_('Inside Country Period Start'),
    )
    in_country_period_end = models.DateField(
        verbose_name=_('Inside Country Period End'),
    )
    resume = models.FileField(
        verbose_name=_('Military Application Resume'),
        upload_to=military_attachment_path_with_user,
    )


    # Status of different parts of the application.
    personal_info_completed = models.BooleanField(
        default=True
    )
    educational_background_completed = models.BooleanField(
        default=False
    )
    postdoc_backgournd_completed = models.BooleanField(
        default=False
    )
    teaching_background_completed = models.BooleanField(
        default=False
    )
    international_papers_completed = models.BooleanField(
        default=False
    )
    internal_papers_completed = models.BooleanField(
        default=False
    )
    conference_papers_completed = models.BooleanField(
        default=False
    )
    research_experience_completed = models.BooleanField(
        default=False
    )
    international_inventions_completed = models.BooleanField(
        default=False
    )
    internal_inventions_completed = models.BooleanField(
        default=False
    )
    offers_completed = models.BooleanField(
        default=False
    )
    scholarships_completed = models.BooleanField(
        default=False
    )
    grants_completed = models.BooleanField(
        default=False
    )
    rankings_completed = models.BooleanField(
        default=False
    )
    olympiads_completed = models.BooleanField(
        default=False
    )
    memberships_completed = models.BooleanField(
        default=False
    )
    editors_memberships_completed = models.BooleanField(
        default=False
    )
    notes_completed = models.BooleanField(
        default=False
    )


class EducationalBackground(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='educational_backgrounds',
    )
    title = models.CharField(
        verbose_name=_('Education Title'),
        max_length=1,
        choices=(
            ('0', 'کارشناسی'),
            ('1', 'کارشناسی ارشد'),
            ('2', 'کارشناسی ارشد پیوسته'),
            ('3', 'دکتری تخخصی'),
            ('4', 'دکتری تخصصی پیوسته'),
            ('5', 'دکتری حرفه‌ای (پزشکی عمومی)'),
        )
    )
    country = models.CharField(
        verbose_name=_('Country of Education'),
        max_length=2,
        choices=COUNTRIES
    )
    education_major = models.CharField(
        max_length=200,
        verbose_name=_('Education Major'),
    )
    university = models.CharField(
        max_length=4,
        verbose_name=_('University of Education'),
        choices=UNIVERSITIES
    )
    photo_of_document = models.FileField(
        verbose_name=_('Photo of the Original Document'),
        upload_to=military_side_attachment_path,
    )
    gpa = models.FloatField(
        verbose_name=_('Average'),
        null=True, blank=True,
        max_length=5
    )
    photo_of_grades = models.FileField(
        verbose_name=_('Photos of Grades'),
        upload_to=military_side_attachment_path,
    )
    vezarat_proof = models.FileField(
        verbose_name=_("Vezarat Oloom Proof"),
        upload_to=military_side_attachment_path,
    )
    start_of_education_date = models.DateTimeField(
        verbose_name=_('Start of Education Date'),
    )
    end_of_education_date = models.DateTimeField(
        verbose_name=_('End of Education Date'),
    )


class PostDocBackground(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='post_docs'
    )
    university = models.CharField(
        max_length=4,
        verbose_name=_('University of Education'),
        choices=UNIVERSITIES_ALL
    )
    photo_of_document = models.FileField(
        upload_to=military_side_attachment_path,
        verbose_name=_('Photo of Postdoc Document')
    )
    start_of_postdoc_date = models.DateTimeField(
        verbose_name=_('Start of Postdoc Date'),
    )
    end_of_postdoc_date = models.DateTimeField(
        verbose_name=_('End of Postdoc Date'),
    )


class TeachingExperience(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='teaching_experiences'
    )
    university = models.CharField(
        max_length=4,
        verbose_name=_('University of Education'),
        choices=UNIVERSITIES_ALL
    )
    type_of_teaching = models.CharField(
        max_length=1,
        choices=(
            ('0', 'Teaching Assistant'),
            ('1', 'Lecturer'),
            ('2', 'Tutor'),
            ('3', 'Lab Instructor'),
            ('4', 'سایر'),
        )
    )
    length = models.IntegerField(
        verbose_name=_('Months of Teaching Experience')
    )
    photo_of_teaching_certificate = models.FileField(
        verbose_name=_('Photo of Teaching Certificate'),
        upload_to=military_side_attachment_path,
    )


class JournalPaper(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='journal_papers',
    )
    paper_title = models.TextField(
        verbose_name=_('Journal Paper Title'),
    )
    journal_title = models.CharField(
        max_length=5,
        verbose_name=_('Journal Title'),
        choices=SC_ISI_JOURNALS
    )
    total_number_of_authors = models.IntegerField(
        verbose_name=_('Total Number of Authors')
    )
    applicants_location_in_authors = models.IntegerField(
        verbose_name=_("Applicant's location in Authors")
    )
    link = models.URLField(
        verbose_name=_("Journal Paper Internet Link")
    )


class InternalResearchPaper(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='internal_journal_papers',
    )
    publish_date = models.DateTimeField(
        verbose_name=_('Publish Date'),
    )
    paper_title = models.TextField(
        verbose_name=_('Journal Paper Title'),
    )
    journal_title = models.CharField(
        max_length=3,
        verbose_name=_('Journal Title'),
        choices=INTERNAL_JOURNALS
    )
    total_number_of_authors = models.IntegerField(
        verbose_name=_('Total Number of Authors')
    )
    applicants_location_in_authors = models.IntegerField(
        verbose_name=_("Applicant's location in Authors")
    )
    link = models.URLField(
        verbose_name=_("Journal Paper Internet Link")
    )


class ConferencePapers(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='conference_papers'
    )
    publish_date = models.DateTimeField(
        verbose_name=_('Publish Date'),
    )
    paper_title = models.TextField(
        verbose_name=_('Journal Paper Title'),
    )
    conference_title = models.TextField(
        verbose_name=_('Conference Title'),
    )
    total_number_of_authors = models.IntegerField(
        verbose_name=_('Total Number of Authors')
    )
    applicants_location_in_authors = models.IntegerField(
        verbose_name=_("Applicant's location in Authors")
    )
    link = models.URLField(
        verbose_name=_("Conference Paper Internet Link")
    )


class ResearchExperience(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='research_experiences',
    )
    title = models.CharField(
        max_length=1,
        choices=(
            ('0', 'Research Assistant'),
            ('1', 'Postdoctoral Researcher'),
            ('0', 'Researcher'),
            ('0', 'سایر'),
        )
    )
    university = models.CharField(
        max_length=4,
        choices=UNIVERSITIES_ALL
    )
    length = models.IntegerField(
        verbose_name=_('Length')
    )
    image_of_research_certificate = models.FileField(
        upload_to=military_side_attachment_path,
        verbose_name=_('Image of Research Certificate')
    )


class InternationalInvention(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='internaional_inventions'
    )
    invention_title = models.TextField(
        verbose_name=_('Invention Title'),
    )
    number_of_all_partners = models.IntegerField(
        verbose_name=_('Number of all Partners')
    )
    applicants_location_in_partners = models.IntegerField(
        verbose_name=_("Applicant's Location in Partners"),
    )
    patent_type = models.CharField(
        max_length=1,
        choices=(
            ('0', "US Patent"),
            ('1', "Euro Patent"),
            ('2', 'سایر')
        )
    )
    link = models.URLField(
        verbose_name=_("Invention URL")
    )


class InternalInvention(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='internal_inventions'
    )
    invention_title = models.TextField(
        verbose_name=_('Invention Title'),
    )
    number_of_all_partners = models.IntegerField(
        verbose_name=_('Number of all Partners')
    )
    applicants_location_in_partners = models.IntegerField(
        verbose_name=_("Applicant's Location in Partners"),
    )
    invention_number = models.IntegerField(
        verbose_name=_("Invention Number")
    )
    certificate = models.FileField(
        upload_to=military_side_attachment_path,
        verbose_name=_("Certificate of Invention"),
    )
    invention_level = models.CharField(
        max_length=1,
        choices=(
            ('0', 'سطح 1'),
            ('1', 'سطح 2'),
            ('2', 'سطح 3'),
        )
    )


class JobOffers(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='job_offers'
    )
    title = models.TextField(
        verbose_name=_('Company Title')
    )
    position = models.TextField(
        verbose_name=_("Job Position")
    )
    start_date = models.DateTimeField(
        verbose_name=_('Job Offer Start Date')
    )
    photo_of_contract = models.FileField(
        upload_to=military_side_attachment_path,
        verbose_name=_('Photo of Contract')
    )


class Scholarship(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='scholarships'
    )
    research_center = models.TextField(
        verbose_name=_('University/Research Center Title')
    )
    scholarship_title = models.TextField(
        verbose_name=_('Scholarship Title'),
    )
    scholarship_type = models.CharField(
        max_length=1,
        choices=(
            ('0', 'Partial'),
            ('1', 'Full')
        )
    )
    scholarship_fund = models.IntegerField(
        verbose_name=_('Scholarship Fund')
    )
    scholarship_currency = models.CharField(
        verbose_name=_('Scholarship Currency'),
        max_length=1,
        choices=(
            ('0', 'دلار'),
            ('1', 'یورو'),
            ('2', 'سایر'),
        )
    )
    start_date = models.DateTimeField(
        verbose_name=_('Scholarship Start Date')
    )
    end_date = models.DateTimeField(
        verbose_name=_('Scholarship End Date')
    )
    photo_of_certificate = models.FileField(
        upload_to=military_attachment_path,
        verbose_name=_('Scholarship Certificate Image')
    )


class ResearchGrant(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='grants'
    )
    research_center = models.TextField(
        verbose_name=_('University/Research Center Title')
    )
    grant_title = models.TextField(
        verbose_name=_('Grant Title'),
    )
    grant_fund = models.IntegerField(
        verbose_name=_('Grant Fund')
    )
    grant_currency = models.CharField(
        verbose_name=_('Grant Currency'),
        max_length=1,
        choices=(
            ('0', 'دلار'),
            ('1', 'یورو'),
            ('2', 'سایر'),
        )
    )
    start_date = models.DateTimeField(
        verbose_name=_('Grant Start Date')
    )
    end_date = models.DateTimeField(
        verbose_name=_('Grant End Date')
    )
    photo_of_certificate = models.FileField(
        upload_to=military_side_attachment_path,
        verbose_name=_('Grant Certificate Image')
    )


class TopRankingBackground(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='ranking_backgrounds'
    )
    type = models.CharField(
        max_length=1,
        verbose_name=_('Top Ranking Type'),
        choices=(
            ('0', 'آزمون ورودی دانشگاه آزاد اسلامی دوره کارشناسی'),
            ('1', 'آزمون سرارسری دوره کارشناسی (وزارت علوم/بهداشت)'),
            ('2', 'کارشناسی ارشد آزمون ورودی دانشگاه آزاد اسلامی'),
            ('3', 'آزمون سراسری دوره کارشناسی ارشد (وزارت علوم/بهداشت)'),
            ('4', 'آزمون ورودی دوره دکتری تخصصی دانشگاه آزاد اسلامی'),
            ('5', 'آزمون سراسری دوره دکتری تخصصی (وزارت علوم/بهداشت)'),
        )
    )
    rank = models.IntegerField(
        verbose_name=_('Rank')
    )
    photo_of_certificate = models.FileField(
        upload_to=military_side_attachment_path,
    )


class OlympiadRanking(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='olympiad_ranking'
    )
    type = models.CharField(
        max_length=1,
        choices=(
            ('0', 'ملی'),
            ('1', 'بین المللی')
        ),
        verbose_name=_('Olympiad Type')
    )
    title = models.CharField(
        max_length=100,
        verbose_name=_("Olympiads Title"),
    )
    ranking_or_medal = models.CharField(
        max_length=1,
        verbose_name=_('Ranking or Medal'),
        choices=(
            ('0', 'رتبه 1/مدال طلا'),
            ('1', 'رتبه 2/مدال نقره'),
            ('2', 'رتبه 3/مدال برنز'),
        )
    )
    photo_of_certificate = models.FileField(
        upload_to=military_side_attachment_path,
    )


class Memberships(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='memberships'
    )
    title_of_association = models.CharField(
        verbose_name=_('Membership Association Title'),
        max_length=300,
    )
    membership_type = models.CharField(
        max_length=1,
        verbose_name=_('Membership Type'),
        choices=(
            ('0', 'دانشجویی/عادی'),
            ('1', 'سایر'),
        )
    )
    length = models.IntegerField(
        verbose_name=_("Membership length"),
    )


class EditorsMembership(models.Model):
    application = models.ForeignKey(
        MilitaryApplication,
        related_name='editors_membership',
    )
    title = models.CharField(
        verbose_name=_("Journal Title"),
        max_length=300,
    )
    position = models.CharField(
        verbose_name=_('Position'),
        max_length=300,
    )
    length = models.IntegerField(
        verbose_name=_('Length')
    )
    photo_of_certificate = models.FileField(
        upload_to=military_attachment_path,
    )


class Notes(models.Model):
    application = models.OneToOneField(
        MilitaryApplication,
    )
    text = models.TextField(
        null=True,
        blank=True,
    )