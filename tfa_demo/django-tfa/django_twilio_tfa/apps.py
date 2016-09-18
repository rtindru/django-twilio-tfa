from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountConfig(AppConfig):
    name = 'django_twilio_tfa'
    verbose_name = _('Django Twilio TFA')
