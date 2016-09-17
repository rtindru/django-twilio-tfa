from functools import wraps

from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.utils.decorators import available_attrs
from django.contrib.auth.decorators import login_required, user_passes_test

from .utils import send_auth_sms, tfa_verify


def tfa_required(auth_url='/tfa/auth', expires=0):
    def dec(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _view(request, *args, **kwargs):
            email = request.user.email
            request.session.set_expiry(expires)
            code = request.session.get('auth_code', None)
            if code:
                return view_func(request, *args, **kwargs)
            send_auth_sms(email)
            next_url = '?next=' + request.path
            red_url = auth_url + next_url
            return HttpResponseRedirect(red_url)
        return login_required(_view)
    return dec
