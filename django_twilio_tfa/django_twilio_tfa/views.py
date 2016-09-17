from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from django.template import loader, Context
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth import logout as auth_logout


from .decorators import tfa_required
from .utils import tfa_verify


class TFAAuthView(TemplateView):
    template_name = 'django_twilio_tfa/auth.html'

    def get_context_data(self, **kwargs):
        context = super(TFAAuthView, self).get_context_data(**kwargs)
        next = self.request.GET.get('next', '/')
        context['next_url'] = next
        return context


class TFAVerifyView(View):

    def post(self, request):
        email = request.user.email
        code = request.POST.get('code')
        next_url = request.POST.get('next', '/')

        resp = tfa_verify(email, code)
        if resp:
            request.session['auth_code'] = code
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, 'Invalid code, please try again')
            red_url = '/tfa/verify' + '?next=' + next_url
            return HttpResponseRedirect(red_url)


@tfa_required()
def home(request):
    context = Context({})
    return render_to_response('django_twilio_tfa/home.html', context)


class HomePageView(TemplateView):

    @method_decorator(tfa_required())
    def dispatch(self, request, *args, **kwargs):
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(HomePageView, self).get_context_data(**kwargs)


def logout(request):
    logout(request)
