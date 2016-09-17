from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib import messages

from .utils import tfa_verify


class TFAAuthView(TemplateView):
    template_name = 'django_twilio_tfa/auth.html'

    def get_context_data(self, **kwargs):
        context = super(TFAAuthView, self).get_context_data(**kwargs)
        next_url = self.request.GET.get('next', '/')
        context['next_url'] = next_url
        return context


class TFAVerifyView(View):

    def post(self, request):
        user = request.user
        code = request.POST.get('code')
        next_url = request.POST.get('next', '/')

        resp = tfa_verify(user, code)
        if resp:
            request.session['auth_code'] = code
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, 'Invalid code, please try again')
            red_url = '/tfa/verify' + '?next=' + next_url
            return HttpResponseRedirect(red_url)
