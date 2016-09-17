from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TFADemoConfig(AppConfig):
    name = 'tfa_demo'
    verbose_name = _('TFA Demo')

    def ready(self):
        from django_twilio_tfa.signal_handlers import *
