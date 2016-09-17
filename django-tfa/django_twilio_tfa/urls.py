from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import *

urlpatterns = patterns('',
    url(r'auth', TFAAuthView.as_view()),
    url(r'verify', TFAVerifyView.as_view()),
)
