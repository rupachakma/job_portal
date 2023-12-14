from django.contrib import admin

from app.models import CustomUser, JobApplication, JobPost

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(JobPost)
admin.site.register(JobApplication)