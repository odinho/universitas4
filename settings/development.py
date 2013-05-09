# Development settings for tutorial
from settings.defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Change this to work with your default development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': project_dir('demo.db'),
    }
}

# URL configuration to use in development mode
ROOT_URLCONF = 'urls.development'

STATICFILES_DIRS = (
    project_dir('static'),
)

INSTALLED_APPS += (
    'importtools',
    'content_replacer',
)

# Attempt to load any settings from settings.local_development, but ignore any
# errors complaining about them not being present.
try:
    from settings.local_development import *
except ImportError, e:
    pass
