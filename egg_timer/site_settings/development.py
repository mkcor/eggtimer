from egg_timer.site_settings.common import *

import os

HOME_DIR = os.path.expanduser("~")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'egg_timer',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
}

MEDIA_ROOT = '/tmp/media'
MEDIA_URL = ''

STATIC_ROOT = '/tmp/static'
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '%s/Development/Django/egg_timer/emails' % HOME_DIR

INSTALLED_APPS.extend([
    'django_nose',
])

# Use nose to run all tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DJANGO_ARGS = [
    '--verbosity=0',
]

NOSE_ARGS = [
    '--verbosity=0',
    '--cover-branches',
    '--cover-package=egg_timer',
    '--cover-inclusive',  # Cover all files
    '--cover-html',
    '--cover-html-dir=%s/egg_timer_coverage' % os.environ.get('HOME'),
]