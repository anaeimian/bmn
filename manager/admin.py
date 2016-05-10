from django.contrib import admin

# Register your models here.
from manager.models import Notice, News

admin.site.register(Notice)
admin.site.register(News)