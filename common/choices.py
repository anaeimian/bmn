#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError:
    _ = lambda x: x

COUNTRIES = (
    ('', '--------'),
    ('IR', _('Iran')),
    ('GB', _('United Kingdom')),
    ('US', _('United States')),
    ('FR', _('France')),
    ('DE', _('Germany')),
    ('KR', _('South Korea')),
    ('RU', _('Russia')),
    ('SY', _('Syria')),
    ('TW', _('Taiwan')),
    ('VE', _('Venezuela')),
    ('VN', _('Vietnam')),
    ('AF', _('Afghanistan')),
    ('AL', _('Albania')),
    ('DZ', _('Algeria')),
    ('AR', _('Argentina')),
    ('AM', _('Armenia')),
    ('AU', _('Australia')),
    ('AT', _('Austria')),
    ('AZ', _('Azerbaijan')),
    ('BH', _('Bahrain')),
    ('BD', _('Bangladesh')),
    ('BY', _('Belarus')),
    ('BE', _('Belgium')),
    ('BA', _('Bosnia and Herzegovina')),
    ('BR', _('Brazil')),
    ('BG', _('Bulgaria')),
    ('CM', _('Cameroon')),
    ('CA', _('Canada')),
    ('TD', _('Chad')),
    ('CL', _('Chile')),
    ('CN', _('China')),
    ('CO', _('Colombia')),
    ('CR', _('Costa Rica')),
    ('HR', _('Croatia')),
    ('CU', _('Cuba')),
    ('CY', _('Cyprus')),
    ('CZ', _('Czech Republic')),
    ('DK', _('Denmark')),
    ('EC', _('Ecuador')),
    ('EG', _('Egypt')),
    ('SV', _('El Salvador')),
    ('FJ', _('Fiji')),
    ('FI', _('Finland')),
    ('GE', _('Georgia')),
    ('GH', _('Ghana')),
    ('GR', _('Greece')),
    ('HK', _('Hong Kong')),
    ('HU', _('Hungary')),
    ('IS', _('Iceland')),
    ('IN', _('India')),
    ('ID', _('Indonesia')),
    ('IQ', _('Iraq')),
    ('IE', _('Ireland')),
    ('IT', _('Italy')),
    ('JM', _('Jamaica')),
    ('JP', _('Japan')),
    ('JO', _('Jordan')),
    ('KZ', _('Kazakhstan')),
    ('KW', _('Kuwait')),
    ('LB', _('Lebanon')),
    ('LY', _('Libya')),
    ('LI', _('Liechtenstein')),
    ('LT', _('Lithuania')),
    ('LU', _('Luxembourg')),
    ('MO', _('Macao')),
    ('MY', _('Malaysia')),
    ('MV', _('Maldives')),
    ('MX', _('Mexico')),
    ('MA', _('Morocco')),
    ('NL', _('Netherlands')),
    ('NZ', _('New Zealand')),
    ('NI', _('Nicaragua')),
    ('NO', _('Norway')),
    ('OM', _('Oman')),
    ('PK', _('Pakistan')),
    ('PS', _('Palestine, State of')),
    ('PY', _('Paraguay')),
    ('PE', _('Peru')),
    ('PH', _('Philippines')),
    ('PL', _('Poland')),
    ('PT', _('Portugal')),
    ('PR', _('Puerto Rico')),
    ('QA', _('Qatar')),
    ('RO', _('Romania')),
    ('SA', _('Saudi Arabia')),
    ('RS', _('Serbia')),
    ('SG', _('Singapore')),
    ('SK', _('Slovakia')),
    ('SI', _('Slovenia')),
    ('ZA', _('South Africa')),
    ('ES', _('Spain')),
    ('SE', _('Sweden')),
    ('CH', _('Switzerland')),
    ('TJ', _('Tajikistan')),
    ('TH', _('Thailand')),
    ('TN', _('Tunisia')),
    ('TR', _('Turkey')),
    ('TM', _('Turkmenistan')),
    ('UA', _('Ukraine')),
    ('AE', _('United Arab Emirates')),
    ('UY', _('Uruguay')),
    ('UZ', _('Uzbekistan')),
    ('YE', _('Yemen')),
)

UNIVERSITIES = (
    ('', '--------'),
    ('MIT', 'Massachusetts Institute of Technology'),
)
UNIVERSITIES_ALL = (
    ('', '--------'),
    ('MIT', 'Massachusetts Institute of Technology'),
)

SC_ISI_JOURNALS = (
    ('', '--------'),
    ('ALO', 'Journal Number One'),
)

INTERNAL_JOURNALS = (
    ('', '--------'),
    ('ALO', 'Journal Number One'),
)

MILITARY_CHOICES = (
    ('0', 'دارای کارت پایان خدمت'),
    ('1', 'مشمول'),
    ('2', 'معاف'),
    ('3', 'هیچکدام')
)

GENDER_CHOICES = (
    ('0', 'زن'),
    ('1', 'مزد'),
)

EDUCATION_CHOICES = (
    ('0', 'دیپلم'),
    ('1', 'لیسانس'),
    ('2', 'فوق لیسانس'),
    ('3', 'دکتری'),
    ('4', 'پسا دکتری'),
)
