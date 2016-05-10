from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import TextInput, ModelChoiceField, ChoiceField
from application.models import CoopApplication
from cons.models import MilitaryApplication
from users.models import BMNUser, Field

__author__ = 'SONY'


# def validate_verify(self):
#     if self.data['password'] != self.data['verify_pass']:
#         print("Raising error!")
#         raise forms.ValidationError(_('Password and verify pass do not match!'))


def validate_email(self):
    if User.objects.filter(email=self):
        raise forms.ValidationError(_('This User Already Exists!'))


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(validators=[validate_email, ])
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'رمز عبور'
            }
        ),
        max_length=100
    )
    verify_pass = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'تکرار رمز عبور'
            }
        ),
        # max_length=100, validators=[validate_verify,]
    )
    field = ModelChoiceField(
        widget=forms.Select,
        queryset=None,
        empty_label='-------',
        label='Please select'
    )

    birthDate = forms.CharField(
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'id': 'birth_date_input',
                'readonly': 'readonly',
                'style': 'text-align: center;',
                'placeholder': 'روز/ماه/سال',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['field'].queryset = Field.objects.all()
        print(self.fields)
        self.fields['first_name'].widget = TextInput(
            attrs={
                'placeholder': 'نام',
            }
        )
        self.fields['last_name'].widget = TextInput(
            attrs={
                'placeholder': 'نام خانوادگی',
            }
        )
        self.fields['email'].widget = TextInput(
            attrs={
                'placeholder': 'example@example.com ',
            }
        )
        self.fields['nationalID'].widget = TextInput(
            attrs={
                'placeholder': 'شماره ملی/ شماره گذرنامه',
            }
        )
        self.fields['email'].widget = TextInput(
            attrs={
                'placeholder': 'example@example.com ',
            }
        )

    class Meta:
        model = BMNUser
        exclude = ['user', 'birth_date']

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        if cleaned_data.get("password") != cleaned_data.get("verify_pass"):
            raise forms.ValidationError(
                "pass and verify pass don't match! "
            )


class CoopApplicationForm(forms.ModelForm):
    class Meta:
        model = CoopApplication
        fields = ['facility', 'field']

    # association1 = ChoiceField(
    #     widget=forms.Select,
    #     # queryset= None,
    #     # empty_label="-------",
    #     # label= 'Select',
    #     required= False
    # )
    # association2 = ModelChoiceField(
    #     widget=forms.Select,
    #     queryset=None,
    #     empty_label='-------',
    #     label = 'Select',
    #     required= False
    # )
    # association3 = ModelChoiceField(
    #     widget=forms.Select,
    #     queryset=None,
    #     empty_label= '-------',
    #     label = 'Select',
    #     required= False
    # )

    # def __init__(self, *args, **kwargs):
    #     super(CoopApplicationForm, self).__init__(*args, **kwargs)
    #     self.fields['association1'].choices = (('hi', 'Sci-Fi'), ('ho', 'Mystery'))
    #     self.fields['association1'].widget.attrs.update({'id': 'id_association1', 'name': 'association1'})
    #     self.fields['association2'].queryset = Association.objects.none()
    #     self.fields['association2'].widget.attrs.update({'id': 'id_association2', 'name': 'association2'})
    #     self.fields['association3'].queryset = Association.objects.none()
    #     self.fields['association3'].widget.attrs.update({'id': 'id_association3', 'name': 'association3'})