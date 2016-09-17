import logging

from django.dispatch import receiver

from .utils import *
from .signals import *

logger = logging.getLogger(__name__)


@receiver(register_user_tfa)
def create_user_tfa_profile(sender, email, phone_number, country_code, **kwargs):
    try:
        tfa_profile = create_tfa_profile(email, phone_number, country_code)
        logger.info(u"TFA Profile Created: {}".format(tfa_profile))
    except Exception as e:
        logger.exception(u"Exception in creating Authy profile".format(e))


@receiver(send_tfa_new_user)
def send_tfa_user(sender, email, phone_number, country_code, **kwargs):
    try:
        tfa_profile = create_tfa_profile(email, phone_number, country_code)
        logger.info(u"TFA Profile Created: {}".format(tfa_profile))
        sms = send_auth_sms(email)
        logger.info(u"SMS Sent: {}".format(sms))
    except Exception as e:
        logger.exception(u"Exception in sending Auth SMS: {}".format(email))
