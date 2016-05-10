from django import forms
from django.forms import TextInput
from cons.models import MilitaryApplication, EducationalBackground, TeachingExperience, JournalPaper, \
    InternalResearchPaper, ResearchExperience, InternalInvention, InternationalInvention, TopRankingBackground, \
    OlympiadRanking, ConferencePapers, JobOffers, Scholarship, ResearchGrant, PostDocBackground, Memberships, \
    EditorsMembership, Notes

__author__ = 'benyamin'


class MilitaryApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MilitaryApplicationForm, self).__init__(*args, **kwargs)
        self.fields['social_id_number'].widget = TextInput(
            attrs={
                'placeholder': 'شماره ملی/ شماره گذرنامه',
            }
        )
        self.fields['begin_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'id': 'in_country_period_start',
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

        self.fields['end_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'id': 'in_country_period_end',
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = MilitaryApplication
        exclude = ['application', 'in_country_period_start', 'in_country_period_end']


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['begin_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

        self.fields['end_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = EducationalBackground
        exclude = ['application', 'end_of_education_date', 'start_of_education_date']


class TeachingForm(forms.ModelForm):
    class Meta:
        model = TeachingExperience
        exclude = ['application']


class InternationalPapersForm(forms.ModelForm):
    class Meta:
        model = JournalPaper
        exclude = ['application']


class InternalPapersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InternalPapersForm, self).__init__(*args, **kwargs)
        self.fields['publish_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = InternalResearchPaper
        exclude = ['application', 'publish_date']


class ResearchExperienceForm(forms.ModelForm):
    class Meta:
        model = ResearchExperience
        exclude = ['application']


class InternalInventionForm(forms.ModelForm):
    class Meta:
        model = InternalInvention
        exclude = ['application']


class InternationalInventionForm(forms.ModelForm):
    class Meta:
        model = InternationalInvention
        exclude = ['application']


class RankingForm(forms.ModelForm):
    class Meta:
        model = TopRankingBackground
        exclude = ['application']


class OlympiadRankingForm(forms.ModelForm):
    class Meta:
        model = OlympiadRanking
        exclude = ['application']


class ConferencePaperForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConferencePaperForm, self).__init__(*args, **kwargs)
        self.fields['publish_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = ConferencePapers
        exclude = ['application', 'publish_date']


class OffersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OffersForm, self).__init__(*args, **kwargs)
        self.fields['start_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = JobOffers
        exclude = ['application', 'start_date']


class ScholarshipForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ScholarshipForm, self).__init__(*args, **kwargs)
        self.fields['start_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )
        self.fields['end_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = Scholarship
        exclude = ['application', 'start_date', 'end_date']


class GrantForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GrantForm, self).__init__(*args, **kwargs)
        self.fields['start_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )
        self.fields['end_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = ResearchGrant
        exclude = ['application', 'start_date', 'end_date']


class PostDocForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostDocForm, self).__init__(*args, **kwargs)
        self.fields['start_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )
        self.fields['end_date'] = forms.CharField(
            max_length=10,
            widget=forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'style': 'text-align: center;',
                    'placeholder': 'روز/ماه/سال',
                }
            )
        )

    class Meta:
        model = PostDocBackground
        exclude = ['application', 'end_of_postdoc_date', 'start_of_postdoc_date']


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Memberships
        exclude = ['application']


class EditorsForm(forms.ModelForm):
    class Meta:
        model = EditorsMembership
        exclude = ['application']


class MyNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ['application']