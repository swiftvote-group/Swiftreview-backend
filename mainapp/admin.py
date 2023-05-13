from django.contrib import admin
from .models import InstitutionProfile, Review

# Register your models here.
admin.site.register(InstitutionProfile)
admin.site.register(Review)