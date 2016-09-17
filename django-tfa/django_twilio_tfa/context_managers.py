from django.conf import settings

from authy.api import AuthyApiClient


class AuthyService(object):
    def __init__(self, api_key=None):
        if api_key is None:
            self.api_key = settings.AUTHY_API_KEY
        else:
            self.api_key = api_key

    def __enter__(self):
        """
        Creates and returns a Google calendar service.
        """
        service = AuthyApiClient(api_key=self.api_key)
        return service

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        XXX: We want to potentially handle some exceptions here and send email to
        admins about Google calendar sync being broken.

        XXX: We should also think of saving the refreshed access token to avoid
        refresh flow every time we want to use the service.
        """
        pass
