# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cons', '0011_auto_20160429_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalbackground',
            name='country',
            field=models.CharField(choices=[('', '--------'), ('IR', 'Iran'), ('GB', 'United Kingdom'), ('US', 'United States'), ('FR', 'France'), ('DE', 'Germany'), ('KR', 'South Korea'), ('RU', 'Russia'), ('SY', 'Syria'), ('TW', 'Taiwan'), ('VE', 'Venezuela'), ('VN', 'Vietnam'), ('AF', 'Afghanistan'), ('AL', 'Albania'), ('DZ', 'Algeria'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AU', 'Australia'), ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BA', 'Bosnia and Herzegovina'), ('BR', 'Brazil'), ('BG', 'Bulgaria'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CO', 'Colombia'), ('CR', 'Costa Rica'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CY', 'Cyprus'), ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('FJ', 'Fiji'), ('FI', 'Finland'), ('GE', 'Georgia'), ('GH', 'Ghana'), ('GR', 'Greece'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'), ('ID', 'Indonesia'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'), ('KW', 'Kuwait'), ('LB', 'Lebanon'), ('LY', 'Libya'), ('LI', 'Liechtenstein'), ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('MX', 'Mexico'), ('MA', 'Morocco'), ('NL', 'Netherlands'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PS', 'Palestine, State of'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RO', 'Romania'), ('SA', 'Saudi Arabia'), ('RS', 'Serbia'), ('SG', 'Singapore'), ('SK', 'Slovakia'), ('SI', 'Slovenia'), ('ZA', 'South Africa'), ('ES', 'Spain'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('TJ', 'Tajikistan'), ('TH', 'Thailand'), ('TN', 'Tunisia'), ('TR', 'Turkey'), ('TM', 'Turkmenistan'), ('UA', 'Ukraine'), ('AE', 'United Arab Emirates'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('YE', 'Yemen')], verbose_name='Country of Education', max_length=2),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='title',
            field=models.CharField(choices=[('0', 'کارشناسی'), ('1', 'کارشناسی ارشد'), ('2', 'کارشناسی ارشد پیوسته'), ('3', 'دکتری تخخصی'), ('4', 'دکتری تخصصی پیوسته'), ('5', 'دکتری حرفه\u200cای (پزشکی عمومی)')], verbose_name='Education Title', max_length=1),
        ),
        migrations.AlterField(
            model_name='educationalbackground',
            name='university',
            field=models.CharField(choices=[('', '--------'), ('MIT', 'Massachusetts Institute of Technology')], verbose_name='University of Education', max_length=4),
        ),
        migrations.AlterField(
            model_name='internalinvention',
            name='invention_level',
            field=models.CharField(choices=[('0', 'سطح 1'), ('1', 'سطح 2'), ('2', 'سطح 3')], max_length=1),
        ),
        migrations.AlterField(
            model_name='internalresearchpaper',
            name='journal_title',
            field=models.CharField(choices=[('', '--------'), ('ALO', 'Journal Number One')], verbose_name='Journal Title', max_length=3),
        ),
        migrations.AlterField(
            model_name='internationalinvention',
            name='patent_type',
            field=models.CharField(choices=[('0', 'US Patent'), ('1', 'Euro Patent'), ('2', 'سایر')], max_length=1),
        ),
        migrations.AlterField(
            model_name='journalpaper',
            name='journal_title',
            field=models.CharField(choices=[('', '--------'), ('ALO', 'Journal Number One')], verbose_name='Journal Title', max_length=5),
        ),
        migrations.AlterField(
            model_name='memberships',
            name='membership_type',
            field=models.CharField(choices=[('0', 'دانشجویی/عادی'), ('1', 'سایر')], verbose_name='Membership Type', max_length=1),
        ),
        migrations.AlterField(
            model_name='militaryapplication',
            name='marital_status',
            field=models.CharField(choices=[('0', 'مجرد'), ('1', 'متاهل')], verbose_name='Marital Status', max_length=1),
        ),
        migrations.AlterField(
            model_name='olympiadranking',
            name='ranking_or_medal',
            field=models.CharField(choices=[('0', 'رتبه 1/مدال طلا'), ('1', 'رتبه 2/مدال نقره'), ('2', 'رتبه 3/مدال برنز')], verbose_name='Ranking or Medal', max_length=1),
        ),
        migrations.AlterField(
            model_name='olympiadranking',
            name='type',
            field=models.CharField(choices=[('0', 'ملی'), ('1', 'بین المللی')], verbose_name='Olympiad Type', max_length=1),
        ),
        migrations.AlterField(
            model_name='postdocbackground',
            name='university',
            field=models.CharField(choices=[('', '--------'), ('MIT', 'Massachusetts Institute of Technology')], verbose_name='University of Education', max_length=4),
        ),
        migrations.AlterField(
            model_name='researchexperience',
            name='title',
            field=models.CharField(choices=[('0', 'Research Assistant'), ('1', 'Postdoctoral Researcher'), ('0', 'Researcher'), ('0', 'سایر')], max_length=1),
        ),
        migrations.AlterField(
            model_name='researchexperience',
            name='university',
            field=models.CharField(choices=[('', '--------'), ('MIT', 'Massachusetts Institute of Technology')], max_length=4),
        ),
        migrations.AlterField(
            model_name='researchgrant',
            name='grant_currency',
            field=models.CharField(choices=[('0', 'دلار'), ('1', 'یورو'), ('2', 'سایر')], verbose_name='Grant Currency', max_length=1),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_currency',
            field=models.CharField(choices=[('0', 'دلار'), ('1', 'یورو'), ('2', 'سایر')], verbose_name='Scholarship Currency', max_length=1),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='scholarship_type',
            field=models.CharField(choices=[('0', 'Partial'), ('1', 'Full')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teachingexperience',
            name='type_of_teaching',
            field=models.CharField(choices=[('0', 'Teaching Assistant'), ('1', 'Lecturer'), ('2', 'Tutor'), ('3', 'Lab Instructor'), ('4', 'سایر')], max_length=1),
        ),
        migrations.AlterField(
            model_name='teachingexperience',
            name='university',
            field=models.CharField(choices=[('', '--------'), ('MIT', 'Massachusetts Institute of Technology')], verbose_name='University of Education', max_length=4),
        ),
        migrations.AlterField(
            model_name='toprankingbackground',
            name='type',
            field=models.CharField(choices=[('0', 'آزمون ورودی دانشگاه آزاد اسلامی دوره کارشناسی'), ('1', 'آزمون سرارسری دوره کارشناسی (وزارت علوم/بهداشت)'), ('2', 'کارشناسی ارشد آزمون ورودی دانشگاه آزاد اسلامی'), ('3', 'آزمون سراسری دوره کارشناسی ارشد (وزارت علوم/بهداشت)'), ('4', 'آزمون ورودی دوره دکتری تخصصی دانشگاه آزاد اسلامی'), ('5', 'آزمون سراسری دوره دکتری تخصصی (وزارت علوم/بهداشت)')], verbose_name='Top Ranking Type', max_length=1),
        ),
    ]
