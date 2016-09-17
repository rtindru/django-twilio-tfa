from django.contrib import admin

from .models import UserProfile

from django_twilio_tfa.context_managers import AuthyService
from django_twilio_tfa.utils import create_tfa_profile


class UserProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
