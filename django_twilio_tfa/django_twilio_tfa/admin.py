from django.contrib import admin

from .models import *


class TFAProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = TFAProfile


admin.site.register(TFAProfile, TFAProfileAdmin)
