from django.contrib import admin

# Register your models here.
from association.models import Facility, Association

admin.site.register(Facility)
admin.site.register(Association)