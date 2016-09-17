from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_twilio_tfa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tfa/auth', TFAAuthView.as_view()),
    url(r'^tfa/verify', TFAVerifyView.as_view()),
    url(r'^home/?$', HomePageView.as_view()),
)
