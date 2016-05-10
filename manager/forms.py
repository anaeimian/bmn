from django.utils.translation import ugettext_lazy as _
from django import forms
from association.models import Facility, Association
from manager.models import Notice, News
from users.models import Field

__author__ = 'benyamin'


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        exclude = ['initiation_date', 'expiration_date']
        error_messages = {
            'title': {
                'required': _('The title cannot be empty')
            },
            'notice_text': {
                'required': _('Notice text cannot be empty')
            }
        }

    start_date = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'start_date_input',
                'readonly': 'readonly',
                'style': 'text-align: center;',
                'placeholder': 'روز/ماه/سال',
            }
        )
    )
    end_date = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'end_date_input',
                'readonly': 'readonly',
                'style': 'text-align: center;',
                'placeholder': 'روز/ماه/سال',
            }
        )
    )


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['creation_date']


class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['title']


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['title']


class AssociationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssociationForm, self).__init__(*args, **kwargs)
        self.fields['facilities'].required = True
        self.fields['fields'].required = True

    class Meta:
        model = Association
        fields = ['fields', 'facilities', 'url', 'logo']


class FilterRequestsForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        required=False
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
    )
    email = forms.EmailField(
        required=False
    )
    field = forms.ModelChoiceField(
        queryset=Field.objects.all(),
        required=False
    )
    facility = forms.ModelChoiceField(
        queryset=Facility.objects.all(),
        required=False
    )
    association = forms.ModelChoiceField(
        queryset=Association.objects.all(),
        required=False
    )
    status = forms.ChoiceField(
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
        required=False
    )
    start_date = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id': 'start_date',
                'readonly': 'readonly',
                'style': 'text-align: center;',
                'placeholder': 'روز/ماه/سال',
            }
        )
    )
    end_date = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id': 'end_date',
                'readonly': 'readonly',
                'style': 'text-align: center;',
                'placeholder': 'روز/ماه/سال',
            }
        )
    )