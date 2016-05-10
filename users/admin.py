from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from users.models import BMNUser, Field, Application

admin.site.register(Field)
admin.site.register(Application)
admin.site.register(BMNUser)
