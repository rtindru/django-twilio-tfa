from django.template import loader, Context
from django.shortcuts import render_to_response
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.views.generic import TemplateView

from django_twilio_tfa.decorators import tfa_required


@tfa_required()
def home(request):
    context = Context({})
    return render_to_response('django_twilio_tfa/home.html', context)


class HomePageView(TemplateView):
    template_name = 'tfa_demo/home.html'

    @method_decorator(tfa_required())
    def dispatch(self, request, *args, **kwargs):
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super(HomePageView, self).get_context_data(**kwargs)


def logout_view(request):
    logout(request)
