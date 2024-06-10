from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry


# Register your models here.

from .models import *

admin.site.register(LearningInstitution)
admin.site.register(Interest)
admin.site.register(User)
admin.site.register(Major)
admin.site.register(UserEducationDetails)
admin.site.register(NotesUpload)
admin.site.register(Waitlist)
admin.site.register(ResourceType)
admin.site.register(Resource)
admin.site.register(ResourceTag)
