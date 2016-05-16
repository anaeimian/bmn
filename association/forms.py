__author__ = 'Arman'
from django import forms
from association.models import Facility, Association
from users.models import Field


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
    # association = forms.ModelChoiceField(
    #     queryset=Association.objects.all(),
    #     required=False
    # )
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