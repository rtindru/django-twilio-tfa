import logging

from django.dispatch import receiver
from django.db.models.signals import post_save

from .utils import *

logger = logging.getLogger(__name__)

user_profile_model = get_user_profile_model()


@receiver(post_save, sender=user_profile_model)
def create_user_tfa_profile(sender, instance, **kwargs):
    try:
        if getattr(instance, uid_field):
            return

        email = getattr(instance, email_field)
        phone = getattr(instance, phone_field)
        cc = getattr(instance, cc_field)

        if not all([email, phone, cc]):
            logger.error("Missing one of email, phone or cc")
            return

        uid = create_tfa_profile(email=email, phone_number=phone, country_code=cc)
        setattr(instance, uid_field, uid)
        instance.save()
    except Exception as e:
        logger.exception(u"Exception in creating Authy profile".format(e))
