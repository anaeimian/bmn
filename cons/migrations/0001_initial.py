# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cons.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConferencePapers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateTimeField(verbose_name='Publish Date')),
                ('paper_title', models.TextField(verbose_name='Journal Paper Title')),
                ('conference_title', models.TextField(verbose_name='Conference Title', choices=[(b'', b'--------'), (b'ALO', b'Journal Number One')])),
                ('total_number_of_authors', models.IntegerField(verbose_name='Total Number of Authors')),
                ('applicants_location_in_authors', models.IntegerField(verbose_name="Applicant's location in Authors")),
                ('link', models.URLField(verbose_name='Conference Paper Internet Link')),
            ],
        ),
        migrations.CreateModel(
            name='EditorsMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.TextField(verbose_name='Position')),
                ('length', models.IntegerField(verbose_name='Length')),
                ('photo_of_certificate', models.FileField(upload_to=cons.models.military_attachment_path)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalBackground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1, verbose_name='Education Title', choices=[(b'0', b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c'), (b'1', b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c \xd8\xa7\xd8\xb1\xd8\xb4\xd8\xaf'), (b'2', b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c \xd8\xa7\xd8\xb1\xd8\xb4\xd8\xaf \xd9\xbe\xdb\x8c\xd9\x88\xd8\xb3\xd8\xaa\xd9\x87'), (b'3', b'\xd8\xaf\xda\xa9\xd8\xaa\xd8\xb1\xdb\x8c \xd8\xaa\xd8\xae\xd8\xae\xd8\xb5\xdb\x8c'), (b'4', b'\xd8\xaf\xda\xa9\xd8\xaa\xd8\xb1\xdb\x8c \xd8\xaa\xd8\xae\xd8\xb5\xd8\xb5\xdb\x8c \xd9\xbe\xdb\x8c\xd9\x88\xd8\xb3\xd8\xaa\xd9\x87'), (b'5', b'\xd8\xaf\xda\xa9\xd8\xaa\xd8\xb1\xdb\x8c \xd8\xad\xd8\xb1\xd9\x81\xd9\x87\xe2\x80\x8c\xd8\xa7\xdb\x8c (\xd9\xbe\xd8\xb2\xd8\xb4\xda\xa9\xdb\x8c \xd8\xb9\xd9\x85\xd9\x88\xd9\x85\xdb\x8c)')])),
                ('country', models.CharField(max_length=2, verbose_name='Country of Education', choices=[(b'', b'--------'), (b'IR', 'Iran'), (b'GB', 'United Kingdom'), (b'US', 'United States'), (b'FR', 'France'), (b'DE', 'Germany'), (b'KR', 'South Korea'), (b'RU', 'Russia'), (b'SY', 'Syria'), (b'TW', 'Taiwan'), (b'VE', 'Venezuela'), (b'VN', 'Vietnam'), (b'AF', 'Afghanistan'), (b'AL', 'Albania'), (b'DZ', 'Algeria'), (b'AR', 'Argentina'), (b'AM', 'Armenia'), (b'AU', 'Australia'), (b'AT', 'Austria'), (b'AZ', 'Azerbaijan'), (b'BH', 'Bahrain'), (b'BD', 'Bangladesh'), (b'BY', 'Belarus'), (b'BE', 'Belgium'), (b'BA', 'Bosnia and Herzegovina'), (b'BR', 'Brazil'), (b'BG', 'Bulgaria'), (b'CM', 'Cameroon'), (b'CA', 'Canada'), (b'TD', 'Chad'), (b'CL', 'Chile'), (b'CN', 'China'), (b'CO', 'Colombia'), (b'CR', 'Costa Rica'), (b'HR', 'Croatia'), (b'CU', 'Cuba'), (b'CY', 'Cyprus'), (b'CZ', 'Czech Republic'), (b'DK', 'Denmark'), (b'EC', 'Ecuador'), (b'EG', 'Egypt'), (b'SV', 'El Salvador'), (b'FJ', 'Fiji'), (b'FI', 'Finland'), (b'GE', 'Georgia'), (b'GH', 'Ghana'), (b'GR', 'Greece'), (b'HK', 'Hong Kong'), (b'HU', 'Hungary'), (b'IS', 'Iceland'), (b'IN', 'India'), (b'ID', 'Indonesia'), (b'IQ', 'Iraq'), (b'IE', 'Ireland'), (b'IT', 'Italy'), (b'JM', 'Jamaica'), (b'JP', 'Japan'), (b'JO', 'Jordan'), (b'KZ', 'Kazakhstan'), (b'KW', 'Kuwait'), (b'LB', 'Lebanon'), (b'LY', 'Libya'), (b'LI', 'Liechtenstein'), (b'LT', 'Lithuania'), (b'LU', 'Luxembourg'), (b'MO', 'Macao'), (b'MY', 'Malaysia'), (b'MV', 'Maldives'), (b'MX', 'Mexico'), (b'MA', 'Morocco'), (b'NL', 'Netherlands'), (b'NZ', 'New Zealand'), (b'NI', 'Nicaragua'), (b'NO', 'Norway'), (b'OM', 'Oman'), (b'PK', 'Pakistan'), (b'PS', 'Palestine, State of'), (b'PY', 'Paraguay'), (b'PE', 'Peru'), (b'PH', 'Philippines'), (b'PL', 'Poland'), (b'PT', 'Portugal'), (b'PR', 'Puerto Rico'), (b'QA', 'Qatar'), (b'RO', 'Romania'), (b'SA', 'Saudi Arabia'), (b'RS', 'Serbia'), (b'SG', 'Singapore'), (b'SK', 'Slovakia'), (b'SI', 'Slovenia'), (b'ZA', 'South Africa'), (b'ES', 'Spain'), (b'SE', 'Sweden'), (b'CH', 'Switzerland'), (b'TJ', 'Tajikistan'), (b'TH', 'Thailand'), (b'TN', 'Tunisia'), (b'TR', 'Turkey'), (b'TM', 'Turkmenistan'), (b'UA', 'Ukraine'), (b'AE', 'United Arab Emirates'), (b'UY', 'Uruguay'), (b'UZ', 'Uzbekistan'), (b'YE', 'Yemen')])),
                ('education_major', models.CharField(max_length=200, verbose_name='Education Major')),
                ('university', models.CharField(max_length=4, verbose_name='University of Education', choices=[(b'', b'--------'), (b'MIT', b'Massachusetts Institute of Technology')])),
                ('photo_of_document', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Photo of the Original Document')),
                ('gpa', models.FloatField(max_length=5, null=True, verbose_name='Average', blank=True)),
                ('photo_of_grades', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Photos of Grades')),
                ('vezarat_proof', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Vezarat Oloom Proof')),
                ('start_of_education_date', models.DateTimeField(verbose_name='Start of Education Date')),
                ('end_of_education_date', models.DateTimeField(verbose_name='End of Education Date')),
            ],
        ),
        migrations.CreateModel(
            name='InternalInvention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invention_title', models.TextField(verbose_name='Invention Title')),
                ('number_of_all_partners', models.IntegerField(verbose_name='Number of all Partners')),
                ('applicants_location_in_partners', models.IntegerField(verbose_name="Applicant's Location in Partners")),
                ('invention_number', models.IntegerField(verbose_name='Invention Number')),
                ('certificate', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Certificate of Invention')),
                ('invention_level', models.CharField(max_length=1, choices=[(b'0', b'\xd8\xb3\xd8\xb7\xd8\xad 1'), (b'1', b'\xd8\xb3\xd8\xb7\xd8\xad 2'), (b'2', b'\xd8\xb3\xd8\xb7\xd8\xad 3')])),
            ],
        ),
        migrations.CreateModel(
            name='InternalResearchPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateTimeField(verbose_name='Publish Date')),
                ('paper_title', models.TextField(verbose_name='Journal Paper Title')),
                ('journal_title', models.CharField(max_length=3, verbose_name='Journal Title', choices=[(b'', b'--------'), (b'ALO', b'Journal Number One')])),
                ('total_number_of_authors', models.IntegerField(verbose_name='Total Number of Authors')),
                ('applicants_location_in_authors', models.IntegerField(verbose_name="Applicant's location in Authors")),
                ('link', models.URLField(verbose_name='Journal Paper Internet Link')),
            ],
        ),
        migrations.CreateModel(
            name='InternationalInvention',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invention_title', models.TextField(verbose_name='Invention Title')),
                ('number_of_all_partners', models.IntegerField(verbose_name='Number of all Partners')),
                ('applicants_location_in_partners', models.IntegerField(verbose_name="Applicant's Location in Partners")),
                ('patent_type', models.CharField(max_length=1, choices=[(b'0', b'US Patent'), (b'1', b'Euro Patent'), (b'2', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')])),
                ('link', models.URLField(verbose_name='Invention URL')),
            ],
        ),
        migrations.CreateModel(
            name='JobOffers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='Company Title')),
                ('position', models.TextField(verbose_name='Job Position')),
                ('start_date', models.DateTimeField(verbose_name='Job Offer Start Date')),
                ('photo_of_contract', models.FileField(upload_to=cons.models.military_attachment_path, verbose_name='Photo of Contract')),
            ],
        ),
        migrations.CreateModel(
            name='JournalPaper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paper_title', models.TextField(verbose_name='Journal Paper Title')),
                ('journal_title', models.CharField(max_length=5, verbose_name='Journal Title', choices=[(b'', b'--------'), (b'ALO', b'Journal Number One')])),
                ('total_number_of_authors', models.IntegerField(verbose_name='Total Number of Authors')),
                ('applicants_location_in_authors', models.IntegerField(verbose_name="Applicant's location in Authors")),
                ('link', models.URLField(verbose_name='Journal Paper Internet Link')),
            ],
        ),
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title_of_association', models.TextField(verbose_name='Membership Association Title')),
                ('membership_type', models.CharField(max_length=1, verbose_name='Membership Type', choices=[(b'0', b'\xd8\xaf\xd8\xa7\xd9\x86\xd8\xb4\xd8\xac\xd9\x88\xdb\x8c\xdb\x8c/\xd8\xb9\xd8\xa7\xd8\xaf\xdb\x8c'), (b'1', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')])),
            ],
        ),
        migrations.CreateModel(
            name='MilitaryApplication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('personneli_photo', models.FileField(upload_to=cons.models.military_attachment_path_with_user, verbose_name='Personneli Photo')),
                ('national_id_photo', models.FileField(upload_to=cons.models.military_attachment_path_with_user, verbose_name='National ID Photo')),
                ('social_id_number', models.CharField(max_length=10, verbose_name='Social ID Number')),
                ('marital_status', models.CharField(max_length=1, verbose_name='Marital Status', choices=[(b'0', b'\xd9\x85\xd8\xac\xd8\xb1\xd8\xaf'), (b'1', b'\xd9\x85\xd8\xaa\xd8\xa7\xd9\x87\xd9\x84')])),
                ('national_booklet_photo', models.FileField(upload_to=cons.models.military_attachment_path_with_user, verbose_name='First Page of National Booklet Photo')),
                ('inner_phone_number', models.CharField(max_length=20, verbose_name='Phone Number Inside Country')),
                ('outer_phone_number', models.CharField(max_length=20, null=True, verbose_name='Phone Number Outside Country', blank=True)),
                ('in_country_period_start', models.DateField(verbose_name='Inside Country Period Start')),
                ('in_country_period_end', models.DateField(verbose_name='Inside Country Period End')),
                ('resume', models.FileField(upload_to=cons.models.military_attachment_path_with_user, verbose_name='Military Application Resume')),
                ('personal_info_completed', models.BooleanField(default=True)),
                ('educational_background_completed', models.BooleanField(default=False)),
                ('teaching_background_completed', models.BooleanField(default=False)),
                ('international_papers_completed', models.BooleanField(default=False)),
                ('internal_papers_completed', models.BooleanField(default=False)),
                ('conference_papers_completed', models.BooleanField(default=False)),
                ('research_experience_completed', models.BooleanField(default=False)),
                ('international_inventions_completed', models.BooleanField(default=False)),
                ('internal_inventions_completed', models.BooleanField(default=False)),
                ('offers_completed', models.BooleanField(default=False)),
                ('scholarships_completed', models.BooleanField(default=False)),
                ('grants_completed', models.BooleanField(default=False)),
                ('rankings_completed', models.BooleanField(default=False)),
                ('olympiads_completed', models.BooleanField(default=False)),
                ('notes_completed', models.BooleanField(default=False)),
                ('application', models.OneToOneField(to='users.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('application', models.OneToOneField(related_name='notes', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='OlympiadRanking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, verbose_name='Olympiad Type', choices=[(b'0', b'\xd9\x85\xd9\x84\xdb\x8c'), (b'1', b'\xd8\xa8\xdb\x8c\xd9\x86 \xd8\xa7\xd9\x84\xd9\x85\xd9\x84\xd9\x84\xdb\x8c')])),
                ('title', models.CharField(max_length=100, verbose_name='Olympiads Title')),
                ('ranking_or_medal', models.CharField(max_length=1, verbose_name='Ranking or Medal', choices=[(b'0', b'\xd8\xb1\xd8\xaa\xd8\xa8\xd9\x87 1/\xd9\x85\xd8\xaf\xd8\xa7\xd9\x84 \xd8\xb7\xd9\x84\xd8\xa7'), (b'1', b'\xd8\xb1\xd8\xaa\xd8\xa8\xd9\x87 2/\xd9\x85\xd8\xaf\xd8\xa7\xd9\x84 \xd9\x86\xd9\x82\xd8\xb1\xd9\x87'), (b'2', b'\xd8\xb1\xd8\xaa\xd8\xa8\xd9\x87 3/\xd9\x85\xd8\xaf\xd8\xa7\xd9\x84 \xd8\xa8\xd8\xb1\xd9\x86\xd8\xb2')])),
                ('photo_of_certificate', models.FileField(upload_to=cons.models.military_side_attachment_path)),
                ('application', models.ForeignKey(related_name='olympiad_ranking', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='PostDocBackground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.CharField(max_length=4, verbose_name='University of Education', choices=[(b'', b'--------'), (b'MIT', b'Massachusetts Institute of Technology')])),
                ('photo_of_document', models.FileField(upload_to=cons.models.military_attachment_path, verbose_name='Photo of Postdoc Document')),
                ('start_of_postdoc_date', models.DateTimeField(verbose_name='Start of Postdoc Date')),
                ('end_of_postdoc_date', models.DateTimeField(verbose_name='End of Postdoc Date')),
                ('application', models.ForeignKey(related_name='post_docs', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1, choices=[(b'0', b'Research Assistant'), (b'1', b'Postdoctoral Researcher'), (b'0', b'Researcher'), (b'0', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')])),
                ('university', models.CharField(max_length=4, choices=[(b'', b'--------'), (b'MIT', b'Massachusetts Institute of Technology')])),
                ('length', models.IntegerField(verbose_name='Length')),
                ('image_of_research_certificate', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Image of Research Certificate')),
                ('application', models.ForeignKey(related_name='research_experiences', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchGrant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('research_center', models.TextField(verbose_name='University/Research Center Title')),
                ('grant_title', models.TextField(verbose_name='Grant Title')),
                ('grant_fund', models.IntegerField(verbose_name='Grant Fund')),
                ('grant_currency', models.CharField(max_length=1, verbose_name='Grant Currency', choices=[(b'0', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1'), (b'1', b'\xdb\x8c\xd9\x88\xd8\xb1\xd9\x88'), (b'2', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1')])),
                ('start_date', models.DateTimeField(verbose_name='Grant Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Grant End Date')),
                ('photo_of_certificate', models.FileField(upload_to=cons.models.military_attachment_path, verbose_name='Grant Certificate Image')),
                ('application', models.ForeignKey(to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('research_center', models.TextField(verbose_name='University/Research Center Title')),
                ('scholarship_title', models.TextField(verbose_name='Scholarship Title')),
                ('scholarship_type', models.CharField(max_length=1, choices=[(b'0', b'Partial'), (b'1', b'Full')])),
                ('scholarship_fund', models.IntegerField(verbose_name='Scholarship Fund')),
                ('scholarship_currency', models.CharField(max_length=1, verbose_name='Scholarship Currency', choices=[(b'0', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1'), (b'1', b'\xdb\x8c\xd9\x88\xd8\xb1\xd9\x88'), (b'2', b'\xd8\xaf\xd9\x84\xd8\xa7\xd8\xb1')])),
                ('start_date', models.DateTimeField(verbose_name='Scholarship Start Date')),
                ('end_date', models.DateTimeField(verbose_name='Scholarship End Date')),
                ('photo_of_certificate', models.FileField(upload_to=cons.models.military_attachment_path, verbose_name='Scholarship Certificate Image')),
                ('application', models.ForeignKey(related_name='scholarships', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='TeachingExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.CharField(max_length=4, verbose_name='University of Education', choices=[(b'', b'--------'), (b'MIT', b'Massachusetts Institute of Technology')])),
                ('type_of_teaching', models.CharField(max_length=1, choices=[(b'0', b'Teaching Assistant'), (b'1', b'Lecturer'), (b'2', b'Tutor'), (b'3', b'Lab Instructor'), (b'4', b'\xd8\xb3\xd8\xa7\xdb\x8c\xd8\xb1')])),
                ('length', models.IntegerField(verbose_name='Months of Teaching Experience')),
                ('photo_of_teaching_certificate', models.FileField(upload_to=cons.models.military_side_attachment_path, verbose_name='Photo of Teaching Certificate')),
                ('application', models.ForeignKey(related_name='teaching_experiences', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.CreateModel(
            name='TopRankingBackground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=1, verbose_name='Top Ranking Type', choices=[(b'0', b'\xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd9\x88\xd8\xb1\xd9\x88\xd8\xaf\xdb\x8c \xd8\xaf\xd8\xa7\xd9\x86\xd8\xb4\xda\xaf\xd8\xa7\xd9\x87 \xd8\xa2\xd8\xb2\xd8\xa7\xd8\xaf \xd8\xa7\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85\xdb\x8c \xd8\xaf\xd9\x88\xd8\xb1\xd9\x87 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c'), (b'1', b'\xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd8\xb3\xd8\xb1\xd8\xa7\xd8\xb1\xd8\xb3\xd8\xb1\xdb\x8c \xd8\xaf\xd9\x88\xd8\xb1\xd9\x87 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c (\xd9\x88\xd8\xb2\xd8\xa7\xd8\xb1\xd8\xaa \xd8\xb9\xd9\x84\xd9\x88\xd9\x85/\xd8\xa8\xd9\x87\xd8\xaf\xd8\xa7\xd8\xb4\xd8\xaa)'), (b'2', b'\xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c \xd8\xa7\xd8\xb1\xd8\xb4\xd8\xaf \xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd9\x88\xd8\xb1\xd9\x88\xd8\xaf\xdb\x8c \xd8\xaf\xd8\xa7\xd9\x86\xd8\xb4\xda\xaf\xd8\xa7\xd9\x87 \xd8\xa2\xd8\xb2\xd8\xa7\xd8\xaf \xd8\xa7\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85\xdb\x8c'), (b'3', b'\xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd8\xb3\xd8\xb1\xd8\xa7\xd8\xb3\xd8\xb1\xdb\x8c \xd8\xaf\xd9\x88\xd8\xb1\xd9\x87 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xb4\xd9\x86\xd8\xa7\xd8\xb3\xdb\x8c \xd8\xa7\xd8\xb1\xd8\xb4\xd8\xaf (\xd9\x88\xd8\xb2\xd8\xa7\xd8\xb1\xd8\xaa \xd8\xb9\xd9\x84\xd9\x88\xd9\x85/\xd8\xa8\xd9\x87\xd8\xaf\xd8\xa7\xd8\xb4\xd8\xaa)'), (b'4', b'\xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd9\x88\xd8\xb1\xd9\x88\xd8\xaf\xdb\x8c \xd8\xaf\xd9\x88\xd8\xb1\xd9\x87 \xd8\xaf\xda\xa9\xd8\xaa\xd8\xb1\xdb\x8c \xd8\xaa\xd8\xae\xd8\xb5\xd8\xb5\xdb\x8c \xd8\xaf\xd8\xa7\xd9\x86\xd8\xb4\xda\xaf\xd8\xa7\xd9\x87 \xd8\xa2\xd8\xb2\xd8\xa7\xd8\xaf \xd8\xa7\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85\xdb\x8c'), (b'5', b'\xd8\xa2\xd8\xb2\xd9\x85\xd9\x88\xd9\x86 \xd8\xb3\xd8\xb1\xd8\xa7\xd8\xb3\xd8\xb1\xdb\x8c \xd8\xaf\xd9\x88\xd8\xb1\xd9\x87 \xd8\xaf\xda\xa9\xd8\xaa\xd8\xb1\xdb\x8c \xd8\xaa\xd8\xae\xd8\xb5\xd8\xb5\xdb\x8c (\xd9\x88\xd8\xb2\xd8\xa7\xd8\xb1\xd8\xaa \xd8\xb9\xd9\x84\xd9\x88\xd9\x85/\xd8\xa8\xd9\x87\xd8\xaf\xd8\xa7\xd8\xb4\xd8\xaa)')])),
                ('rank', models.IntegerField(verbose_name='Rank')),
                ('photo_of_certificate', models.FileField(upload_to=cons.models.military_side_attachment_path)),
                ('application', models.ForeignKey(related_name='ranking_backgrounds', to='cons.MilitaryApplication')),
            ],
        ),
        migrations.AddField(
            model_name='memberships',
            name='application',
            field=models.ForeignKey(related_name='memberships', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='journalpaper',
            name='application',
            field=models.ForeignKey(related_name='journal_papers', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='joboffers',
            name='application',
            field=models.ForeignKey(related_name='job_offers', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='internationalinvention',
            name='application',
            field=models.ForeignKey(related_name='internaional_inventions', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='internalresearchpaper',
            name='application',
            field=models.ForeignKey(related_name='internal_journal_papers', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='internalinvention',
            name='application',
            field=models.ForeignKey(related_name='internal_inventions', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='educationalbackground',
            name='application',
            field=models.ForeignKey(related_name='educational_backgrounds', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='editorsmembership',
            name='application',
            field=models.ForeignKey(related_name='editors_membership', to='cons.MilitaryApplication'),
        ),
        migrations.AddField(
            model_name='conferencepapers',
            name='application',
            field=models.ForeignKey(related_name='conference_papers', to='cons.MilitaryApplication'),
        ),
    ]
