from django.contrib import admin
from .models import CustomUser, Profile, ResetToken

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(ResetToken)