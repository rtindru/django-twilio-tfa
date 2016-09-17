from django.apps import apps as django_apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


from .context_managers import AuthyService
from .models import TFAProfile


def get_user_model():
    """
    Returns the User model that is active in this project.
    """
    try:
        return django_apps.get_model(settings.USER_MODEL)
    except ValueError:
        raise ImproperlyConfigured("USER_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "USER_MODEL refers to model '%s' that has not been installed" % settings.AUTH_USER_MODEL
        )


def create_tfa_profile(email, phone_number, country_code):
    with AuthyService() as service:
        user = service.users.create(email, phone_number, country_code)
        if user.ok():
            tfa_profile = TFAProfile.objects.get_or_create(
                email=email,
                defaults={
                    'authy_id': user.id,
                    'phone_number': phone_number,
                    'country_code': country_code
                }
            )
            return tfa_profile
        else:
            raise Exception(user.errors())


def send_auth_sms(email):
    tfa_profile = TFAProfile.objects.get(email=email)
    with AuthyService() as service:
        sms = service.users.request_sms(tfa_profile.authy_id, {'force': True})
        if sms.ok():
            return sms
        else:
            raise Exception(sms.errors())


def tfa_verify(email, code):
    tfa_profile = TFAProfile.objects.get(email=email)
    with AuthyService() as service:
        verification = service.tokens.verify(tfa_profile.authy_id, code)
        if verification.ok():
            return True
        else:
            return False
