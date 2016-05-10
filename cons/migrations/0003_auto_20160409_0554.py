# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0002_auto_20160409_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalbackground',
            name='title',
            field=models.CharField(max_length=1, choices=[('0', 'کارشناسی'), ('1', 'کارشناسی ارشد'), ('2', 'کارشناسی ارشد پیوسته'), ('3', 'دکتری تخخصی'), ('4', 'دکتری تخصصی پیوسته'), ('5', 'دکتری حرفه\u200cای (پزشکی عمومی)')], verbose_name='Education Title'),
        ),
        migrations.AlterField(
            model_name='internalinvention',
            name='invention_level',
            field=models.CharField(max_length=1, choices=[('0', 'سطح 1'), ('1', 'سطح 2'), ('2', 'سطح 3')]),
        ),
        migrations.AlterField(
            model_name='internationalinvention',
            name='patent_type',
            field=models.CharField(max_length=1, choices=[('0', 'US Patent'), ('1', 'Euro Patent'), ('2', 'سایر')]),
        ),
        migrations.AlterField(
            model_name='memberships',
            name='membership_type',
            field=models.CharField(max_length=1, choices=[('0', 'دانشجویی/عادی'), ('1', 'سایر')], verbose_name='Membership Type'),
        ),
        migrations.AlterField(
            model_name='militaryapplication',
            name='marital_status',
            field=models.CharField(max_length=1, choices=[('0', 'مجرد'), ('1', 'متاهل')], verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='olympiadranking',
            name='ranking_or_medal',
            field=models.CharField(max_length=1, choices=[('0', 'رتبه 1/مدال طلا'), ('1', 'رتبه 2/مدال نقره'), ('2', 'رتبه 3/مدال برنز')], verbose_name='Ranking or Medal'),
        ),
        migrations.AlterField(
            model_name='olympiadranking',
            name='type',
            field=models.CharField(max_length=1, choices=[('0', 'ملی'), ('1', 'بین المللی')], verbose_name='Olympiad Type'),
        ),
        migrations.AlterField(
            model_name='researchexperience',
            name='title',
            field=models.CharField(max_length=1, choices=[('0', 'Research Assistant'), ('1', 'Postdoctoral Researcher'), ('0', 'Researcher'), ('0', 'سایر')]),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='grant_currency',
            field=models.CharField(max_length=1, choices=[('0', 'دلار'), ('1', 'یورو'), ('2', 'دلار')], verbose_name='Grant Currency'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_currency',
            field=models.CharField(max_length=1, choices=[('0', 'دلار'), ('1', 'یورو'), ('2', 'دلار')], verbose_name='Scholarship Currency'),
        ),
        migrations.AlterField(
            model_name='teachingexperience',
            name='type_of_teaching',
            field=models.CharField(max_length=1, choices=[('0', 'Teaching Assistant'), ('1', 'Lecturer'), ('2', 'Tutor'), ('3', 'Lab Instructor'), ('4', 'سایر')]),
        ),
        migrations.AlterField(
            model_name='toprankingbackground',
            name='type',
            field=models.CharField(max_length=1, choices=[('0', 'آزمون ورودی دانشگاه آزاد اسلامی دوره کارشناسی'), ('1', 'آزمون سرارسری دوره کارشناسی (وزارت علوم/بهداشت)'), ('2', 'کارشناسی ارشد آزمون ورودی دانشگاه آزاد اسلامی'), ('3', 'آزمون سراسری دوره کارشناسی ارشد (وزارت علوم/بهداشت)'), ('4', 'آزمون ورودی دوره دکتری تخصصی دانشگاه آزاد اسلامی'), ('5', 'آزمون سراسری دوره دکتری تخصصی (وزارت علوم/بهداشت)')], verbose_name='Top Ranking Type'),
        ),
    ]
