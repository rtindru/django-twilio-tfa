from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured
from django.db.models import FieldDoesNotExist

from .context_managers import AuthyService
from .models import TFAProfile
import app_settings

uid_field = app_settings.USER_UID_FIELD
email_field = app_settings.USER_EMAIL_FIELD
phone_field = app_settings.USER_PHONE_FIELD
cc_field = app_settings.USER_CC_FIELD


def get_user_profile_model():
    """
    Returns the User model that is active in this project.
    """
    try:
        return django_apps.get_model(app_settings.USER_PROFILE_MODEL)
    except AttributeError:
        raise ImproperlyConfigured("USER_PROFILE_MODEL is not defined in settings")
    except ValueError:
        raise ImproperlyConfigured("USER_PROFILE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "USER_PROFILE_MODEL refers to model '%s' that has not been installed" % app_settings.USER_PROFILE_MODEL
        )


def create_tfa_profile(email, phone_number, country_code):
    with AuthyService() as service:
        user = service.users.create(email, phone_number, country_code)
        if user.ok():
            return user.id
        else:
            raise Exception(user.errors())


def send_auth_sms(user):
    user_profile_model = get_user_profile_model()
    user_profile = user_profile_model.objects.get(user=user)
    with AuthyService() as service:
        uid = getattr(user_profile, uid_field)
        sms = service.users.request_sms(uid, {'force': True})
        if sms.ok():
            return sms
        else:
            raise Exception(sms.errors())


def tfa_verify(user, code):
    user_profile_model = get_user_profile_model()
    user_profile = user_profile_model.objects.get(user=user)
    with AuthyService() as service:
        uid = getattr(user_profile, uid_field)
        verification = service.tokens.verify(uid, code)
        if verification.ok():
            return True
        else:
            return False
