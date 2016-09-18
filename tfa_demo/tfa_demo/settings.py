"""
Django settings for tfa_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wp0ng=xjbxnn8xn)yx@rn)q6u*fjtyivji22_dclz9omq_9m-o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_twilio_tfa',
    'tfa_demo',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
"""
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'allauth.socialaccount.context_processors.socialaccount',
    'django.template.context_processors.request',
)
"""
ROOT_URLCONF = 'tfa_demo.urls'

WSGI_APPLICATION = 'tfa_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(filename)s:%(lineno)d:%(funcName)s:: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'exc_file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/tmp/exc.log',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/deb.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file', 'exc_file', 'console'],
        'level': 'DEBUG',
    },
}

TEMPLATE_DIRS = (
    # allauth templates: you could copy this directory into your
    # project and tweak it according to your needs
    # os.path.join(PROJECT_ROOT, 'templates', 'uniform', 'allauth'),
    # example project specific templates
    os.path.join(BASE_DIR, 'templates', 'plain', 'example'),
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# AUTHY_API_KEY = 'dI5MxJYUlu8ar8RJLismMSqMIBmaDte7'
AUTHY_API_KEY = '7TZVaaHRxoio4Ot4fg9BWExc9ZCSQ8cE'
USER_PROFILE_MODEL = 'tfa_demo.UserProfile'

ACCOUNT_SIGNUP_FORM_CLASS = "tfa_demo.forms.SignupForm"

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = None
