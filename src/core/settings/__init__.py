import os
import datetime
import logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Include the right settings
try:
    from .local import *
except ImportError as e:
    from .production import *

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'scrap_data',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
GOOGLE_ANALYTICS_MODEL = True

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '..', '..', 'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '..', '..', 'static'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True
