from django import template
from django.forms import ClearableFileInput, FileField
import jdatetime

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name='is_inputfile')
def is_inputfile(obj):
    return obj.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__


@register.filter(name='is_required', is_safe=True)
def is_required(obj):
    if obj.field.required:
        return obj.label_tag(attrs={'class': 'star'})
    else:
        return obj.label_tag()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def to_jdate(date):
    return jdatetime.datetime.fromgregorian(datetime=date).strftime('%Y/%m/%d')