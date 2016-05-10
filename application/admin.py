from django.contrib import admin

# Register your models here.
from application.models import TextExtraAttachment, FileExtraAttachment, RequirementField, Association_Application, \
    CoopApplication

admin.site.register(TextExtraAttachment)
admin.site.register(FileExtraAttachment)
admin.site.register(RequirementField)
admin.site.register(CoopApplication)
admin.site.register(Association_Application)
