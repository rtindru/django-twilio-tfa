# django-twilio-tfa
Pluggable module for Two factor authentication using Twilio Authy

=====
Django Two Factor Authentication
=====

Django TFA is a simple Django app to add two factor authentication to your Django projects super quickly! It's as simple as adding a decorator your views!

Detailed documentation is in the "docs" directory.

Installation
-----------
The installer package is available under django-tfa/dist/

**Example:**

`pip install django-tfa-0.1.1.tar.gz `


Quick start
-----------
    
1. Add "django_twilio_tfa" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_twilio_tfa',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^tfa/', include('django_twilio_tfa.urls')),


3. Add "AUTHY_API_KEY" to settings.py

4. Add "USER_PROFILE_MODEL" to your settings.py. The "USER_PROFILE_MODEL" should have a one-to-one field with the User model.

5. The following fields should be available on the USER_PROFILE_MODEL defined above. To edit the field names add the following to settings.py:
    a. USER_UID_FIELD: Defaults to "uid" - This field should be writable.
    b. USER_EMAIL_FIELD: Defaults to "email"
    c. USER_PHONE_FIELD: Defaults to "phone"
    d. USER_CC_FIELD: Defaults to "country_code"

