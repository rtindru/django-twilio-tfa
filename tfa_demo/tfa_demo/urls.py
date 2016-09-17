from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    url(r'^accounts/', include('allauth.urls')),
    url(r'^tfa/', include('django_twilio_tfa.urls')),
    url(r'^$', HomePageView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/?$', HomePageView.as_view()),
    url(r'^logout/?', logout),
)
