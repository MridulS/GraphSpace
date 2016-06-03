"""
Django settings for graphspace project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

## Most of the settings in this file are automatically generated when automatically creating the project. I have added comments (starting with two hashes) before every line that I have modified.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import local_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = local_settings.getSecretKey()

# Amazon Mechanical Turk Keys (http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.html)
AWSACCESSKEYID = local_settings.getAWSKey()
SECRETKEY = local_settings.getAWSSecretKey()
AWS_URL = local_settings.getAWSURL()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = local_settings.getDebug()

TEMPLATE_DEBUG = local_settings.getTemplateDebug()

ALLOWED_HOSTS = ['*']

# GLOBAL VALUES FOR DATABASE AND PATHS
DB_FULL_PATH = os.path.join(BASE_DIR, 'graphspace.db')
URL_PATH = local_settings.getURLPath()
DATABASE_LOCATION = 'sqlite:///' + DB_FULL_PATH
GOOGLE_ANALYTICS_PROPERTY_ID = local_settings.getGoogleAnalyticsId()

# Application definition

INSTALLED_APPS = (
    'analytical',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'graphs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware'

)

ROOT_URLCONF = 'graphspace.urls'

WSGI_APPLICATION = 'graphspace.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'graphspace.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

## Changed from 'UTC'.
TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email setup
EMAIL_USE_TLS = True
EMAIL_HOST = local_settings.getEmailHost()
EMAIL_HOST_USER = local_settings.getEmailUser()
EMAIL_HOST_PASSWORD = local_settings.getEmailPassword()
EMAIL_PORT = 587

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

## for authentication. Since we need to use SQL Alchemy for the ORM, we cannot use the authentication backend automatically provided by Django when using the Django ORM.
AUTHENTICATION_BACKENDS = ('graphs.auth.AuthBackend.AuthBackend',)

## Following the recommendation of the Django tutorial at
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        }
    },
}
DEBUG_PROPAGATE_EXCEPTIONS = True
