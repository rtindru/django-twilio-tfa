from django.db import models


class TFAProfile(models.Model):
    authy_id = models.IntegerField(unique=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    country_code = models.IntegerField()

    def __unicode__(self):
        return u"{}, {}".format(self.authy_id, self.email)
