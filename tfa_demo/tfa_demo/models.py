from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    uid = models.IntegerField(unique=True, null=True, blank=True)
    user = models.OneToOneField(User)
    phone = models.IntegerField()
    country_code = models.IntegerField()

    def __unicode__(self):
        return u"{}, +{} {}".format(self.user.username, self.country_code, self.phone)

    @property
    def email(self):
        return self.user.email