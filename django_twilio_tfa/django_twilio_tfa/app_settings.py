from django.conf import settings

USER_PROFILE_MODEL = getattr(settings, 'USER_PROFILE_MODEL')
USER_UID_FIELD = getattr(settings, 'USER_UID_FIELD', 'uid')
USER_EMAIL_FIELD = getattr(settings, 'USER_EMAIL_FIELD', 'email')
USER_PHONE_FIELD = getattr(settings, 'USER_PHONE_FIELD', 'phone')
USER_CC_FIELD = getattr(settings, 'USER_CC_FIELD', 'country_code')
