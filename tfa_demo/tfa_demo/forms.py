from django.contrib.auth import get_user_model
from django import forms

from .models import UserProfile


class SignupForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['phone', 'country_code']

    def signup(self, request, user):
        phone = self.cleaned_data['phone']
        country_code = self.cleaned_data['country_code']
        profile = UserProfile.objects.get_or_create(
            user=user, phone=phone, country_code=country_code
        )
