from django.contrib import admin
from messaging.models import Message, Conversation

admin.site.register(Message)
admin.site.register(Conversation)
# Register your models here.
