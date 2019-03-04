import os
# import environ
import oscar


# env = environ.Env()

# Path helper
location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

DEBUG = True

ALLOWED_HOSTS = [
    'latest.oscarcommerce.com',
    'master.oscarcommerce.com',
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
]

WSGI_APPLICATION = 'frobshop.wsgi.application'

# This is needed for the hosted version of the sandbox
ADMINS = (
    ('William Lee', 'bill00lee@gmail.com'),
)
EMAIL_SUBJECT_PREFIX = '[Oscar sandbox] '
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MANAGERS = ADMINS

# # Use a Sqlite database by default
# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
#         'NAME': os.environ.get('DATABASE_NAME', location('db.sqlite')),
#         'USER': os.environ.get('DATABASE_USER', None),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD', None),
#         'HOST': os.environ.get('DATABASE_HOST', None),
#         'PORT': os.environ.get('DATABASE_PORT', None),
#         'ATOMIC_REQUESTS': True
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database1',
        'USER': 'database1_role',
        'PASSWORD': 'database1_password',
        'HOST': 'database1',  # <-- IMPORTANT: same name as docker-compose service!
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

# CACHES = {
#     'default': env.cache(default='locmemcache://'),
# }


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
USE_TZ = True
TIME_ZONE = 'America/Toronto'

# TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# Includes all languages that have >50% coverage in Transifex
# Taken from Django's default setting for LANGUAGES
gettext_noop = lambda s: s
LANGUAGES = (
    ('ar', gettext_noop('Arabic')),
    ('ca', gettext_noop('Catalan')),
    ('cs', gettext_noop('Czech')),
    ('da', gettext_noop('Danish')),
    ('de', gettext_noop('German')),
    ('en-gb', gettext_noop('British English')),
    ('el', gettext_noop('Greek')),
    ('es', gettext_noop('Spanish')),
    ('fi', gettext_noop('Finnish')),
    ('fr', gettext_noop('French')),
    ('it', gettext_noop('Italian')),
    ('ko', gettext_noop('Korean')),
    ('nl', gettext_noop('Dutch')),
    ('pl', gettext_noop('Polish')),
    ('pt', gettext_noop('Portuguese')),
    ('pt-br', gettext_noop('Brazilian Portuguese')),
    ('ro', gettext_noop('Romanian')),
    ('ru', gettext_noop('Russian')),
    ('sk', gettext_noop('Slovak')),
    ('uk', gettext_noop('Ukrainian')),
    ('zh-cn', gettext_noop('Simplified Chinese')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = location("public/media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = location('public/static')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATICFILES_DIRS = (
    location('static/'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p}{:][;'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            location('templates'),
            oscar.OSCAR_MAIN_TEMPLATE_DIR,
        ],
        'OPTIONS': {
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                # Oscar specific
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.core.context_processors.metadata',
            ],
            'debug': DEBUG,
        }
    }
]

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',

    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Allow languages to be selected
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Ensure a valid basket is added to the request instance for every request
    'oscar.apps.basket.middleware.BasketMiddleware',
]

ROOT_URLCONF = 'frobshop.urls'


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(message)s',
#         },
#         'simple': {
#             'format': '[%(asctime)s] %(message)s'
#         },
#     },
#     'root': {
#         'level': 'DEBUG',
#         'handlers': ['console'],
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#     },
#     'loggers': {
#         'oscar': {
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'oscar.catalogue.import': {
#             'handlers': ['console'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#         'oscar.alerts': {
#             'handlers': ['null'],
#             'level': 'INFO',
#             'propagate': False,
#         },
#
#         # Django loggers
#         'django': {
#             'handlers': ['null'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['console'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         'django.db.backends': {
#             'level': 'WARNING',
#             'propagate': True,
#         },
#         'django.security.DisallowedHost': {
#             'handlers': ['null'],
#             'propagate': False,
#         },
#
#         # Third party
#         'raven': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#             'propagate': False,
#         },
#         'sorl.thumbnail': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#     }
# }

from oscar import get_core_apps

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',
    # ...
    'compressor',
    'widget_tweaks',
] + get_core_apps()

SITE_ID = 1

# Add Oscar's custom auth backend so users can sign in using their email
# address.

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 9,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True

# ====================
# Messages contrib app
# ====================

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
# Here's a sample Haystack config if using Solr (which is recommended)
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8983/solr/oscar_latest/',
#        'INCLUDE_SPELLING': True
#    },
#}

# =============
# Debug Toolbar
# =============

# INTERNAL_IPS = ['127.0.0.1', '::1', "*"]

# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# Meta
# ====

OSCAR_SHOP_TAGLINE = 'Sandbox'

OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True


# Order processing
# ================

# Sample order/line status settings. This is quite simplistic. It's like you'll
# want to override the set_status method on the order object to do more
# sophisticated things.
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Complete', 'Cancelled',),
    'Cancelled': (),
    'Complete': (),
}

# This dict defines the line statuses that will be set when an order's status
# is changed
OSCAR_ORDER_STATUS_CASCADE = {
    'Being processed': 'Being processed',
    'Cancelled': 'Cancelled',
    'Complete': 'Shipped',
}

# LESS/CSS
# ========

# We default to using CSS files, rather than the LESS files that generate them.
# If you want to develop Oscar's CSS, then set OSCAR_USE_LESS=True to enable the
# on-the-fly less processor.
OSCAR_USE_LESS = False


# Sentry
# ======
#
# if env('SENTRY_DSN', default=None):
#     RAVEN_CONFIG = {'dsn': env('SENTRY_DSN', default=None)}
#     LOGGING['handlers']['sentry'] = {
#         'level': 'ERROR',
#         'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
#     }
#     LOGGING['root']['handlers'].append('sentry')
#     INSTALLED_APPS.append('raven.contrib.django.raven_compat')
#
#
# # Sorl
# # ====
#
# THUMBNAIL_DEBUG = DEBUG
# THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'
# THUMBNAIL_KVSTORE = env(
#     'THUMBNAIL_KVSTORE',
#     default='sorl.thumbnail.kvstores.cached_db_kvstore.KVStore')
# THUMBNAIL_REDIS_URL = env('THUMBNAIL_REDIS_URL', default=None)
#
#
# # Django 1.6 has switched to JSON serializing for security reasons, but it does not
# # serialize Models. We should resolve this by extending the
# # django/core/serializers/json.Serializer to have the `dumps` function. Also
# # in tests/config.py
# SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
#
# # Try and import local settings which can be used to override any of the above.
# try:
#     from settings_local import *
# except ImportError:
#     pass
#
#

# import os
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# # Django settings for oscar project.
# PROJECT_DIR = os.path.dirname(__file__)
# location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
#
# DEBUG = True
# TEMPLATE_DEBUG = True
# SQL_DEBUG = True
#
# ADMINS = (
#     # ('Your Name', 'your_email@domain.com'),
# )
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# USE_TZ = True
#
# MANAGERS = ADMINS
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': location('db.sqlite'),                      # Or path to database file if using sqlite3.
#         'USER': '',                      # Not used with sqlite3.
#         'PASSWORD': '',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }
# ATOMIC_REQUESTS = True
#
# # Local time zone for this installation. Choices can be found here:
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # although not all choices may be available on all operating systems.
# # On Unix systems, a value of None will cause Django to use the same
# # timezone as the operating system.
# # If running in a Windows environment this must be set to the same as your
# # system time zone.
# TIME_ZONE = 'America/Toronto'
#
# # Language code for this installation. All choices can be found here:
# # http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-ca'
#
# gettext_noop = lambda s: s
# LANGUAGES = (
#     ('en-ca', gettext_noop('Canada')),
#     ('zh-cn', gettext_noop('Simplified Chinese')),
#     ('es', gettext_noop('Spanish')),
# )
#
# SITE_ID = 1
#
# # If you set this to False, Django will make some optimizations so as not
# # to load the internationalization machinery.
# USE_I18N = True
#
# # If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale
# USE_L10N = True
#
# # Absolute path to the directory that holds media.
# # Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = location("public/media")
#
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash if there is a path component (optional in other cases).
# # Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = '/media/'
#
# # URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# # trailing slash.
# # Examples: "http://foo.com/media/", "/media/".
# #ADMIN_MEDIA_PREFIX = '/media/admin/'
#
# STATIC_URL = '/static/'
# STATIC_ROOT = location('public')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
#
# # Make this unique, and don't share it with anybody.
# SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p#!)n1a'
#
# MIDDLEWARE = (
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'oscar.apps.basket.middleware.BasketMiddleware',
# )
#
# INTERNAL_IPS = ('127.0.0.1',)
#
# ROOT_URLCONF = 'urls'
#
# from oscar import OSCAR_MAIN_TEMPLATE_DIR
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             location('templates'),
#             os.path.join(OSCAR_MAIN_TEMPLATE_DIR, 'templates'),
#             OSCAR_MAIN_TEMPLATE_DIR,
#         ],
#         'OPTIONS': {
#             'loaders': [
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#             ],
#             'context_processors': [
#                 'django.contrib.auth.context_processors.auth',
#                 'django.template.context_processors.request',
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.i18n',
#                 'django.template.context_processors.media',
#                 'django.template.context_processors.static',
#                 'django.contrib.messages.context_processors.messages',
#
#                 'oscar.apps.search.context_processors.search_form',
#                 'oscar.apps.promotions.context_processors.promotions',
#                 'oscar.apps.checkout.context_processors.checkout',
#                 'oscar.core.context_processors.metadata',
#             ],
#         }
#     }
# ]
#
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['null'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'oscar.checkout': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.db.backends': {
#             'handlers': ['null'],
#             'propagate': False,
#             'level': 'DEBUG',
#         },
#         'paypal.express': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#         'paypal.payflow': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }
#
#
# INSTALLED_APPS = [
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.admin',
#     'django.contrib.flatpages',
#     'django.contrib.staticfiles',
#     # External apps
#     'django_extensions',
#     'debug_toolbar',
#     # Apps from oscar
#     'paypal',
#     'widget_tweaks',
# ]
#
#
#
# from oscar import get_core_apps
# INSTALLED_APPS = INSTALLED_APPS + get_core_apps([
#     'apps.shipping',
#     'apps.order',
#     'apps.catalogue',
#     'apps.checkout'])
#
# AUTHENTICATION_BACKENDS = (
#     'oscar.apps.customer.auth_backends.EmailBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# LOGIN_REDIRECT_URL = '/accounts/'
# APPEND_SLASH = True
#
# # Oscar settings
# from oscar.defaults import *
# OSCAR_ALLOW_ANON_CHECKOUT = True
#
# OSCAR_SHOP_TAGLINE = 'PayPal'
#
# # Add Payflow dashboard stuff to settings
# from django.utils.translation import ugettext_lazy as _
# OSCAR_DASHBOARD_NAVIGATION.append(
#     {
#         'label': _('PayPal'),
#         'icon': 'icon-globe',
#         'children': [
#             {
#                 'label': _('PayFlow transactions'),
#                 'url_name': 'paypal-payflow-list',
#             },
#             {
#                 'label': _('Express transactions'),
#                 'url_name': 'paypal-express-list',
#             },
#         ]
#     })
#
#
# # Haystack settings
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }
#
# # Taken from PayPal's documentation - these should always work in the sandbox
# PAYPAL_SANDBOX_MODE = True
# PAYPAL_CALLBACK_HTTPS = False
# PAYPAL_API_VERSION = '119'
#
# # These are the standard PayPal sandbox details from the docs - but I don't
# # think you can get access to the merchant dashboard.
#
#
# PAYPAL_API_USERNAME = 'EelConsultancy-facilitator_api1.gmail.com'
# PAYPAL_API_PASSWORD = '5T2A9NCXZNMBVN2E'
# PAYPAL_API_SIGNATURE = 'A1GGT.a.X8D3d-gBBE6E7iuU2TIeAASCDi8zyqSWdybdQo04FcEsc8g3'
#
# # http://127.0.0.1:8000/static/assets/images/logo2.png
#
#
# # Standard currency is CAD
# PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'CAD'
# PAYPAL_PAYFLOW_DASHBOARD_FORMS = True
#
# # Put your own sandbox settings into an integration.py modulde (that is ignored
# # by git).
# try:
#     from integration import *  # noqa
# except ImportError:
#     pass
#
# OSCAR_INITIAL_ORDER_STATUS = 'Pending'
#
#
# # This dict defines the new order statuses than an order can move to
# OSCAR_ORDER_STATUS_PIPELINE = {
#     'Pending': ('Being processed', 'Cancelled',),
#     'Being processed': ('Complete', 'Cancelled',),
#     'Cancelled': ('Pending', 'Being processed', 'Cancelled',),
#     'Complete': ('Pending', 'Being processed', 'Cancelled',),
# }
#
# # This dict defines the line statuses that will be set when an order's status
# # is changed
# # OSCAR_ORDER_STATUS_CASCADE = {
# #      'Pending': ('Being processed', 'Cancelled',),
# #      'Being processed': ('Complete', 'Cancelled',),
# #      'Complete': 'Cancelled',
# #      'Cancelled': ('Being processed', 'Cancelled',),
# # }
#
# OSCAR_INITIAL_LINE_STATUS = 'Pending'
# OSCAR_LINE_STATUS_PIPELINE = {
#     'Pending': ('Partner Confirmed', 'Cancelled',),
#     'Partner Confirmed': ('Picked up', 'Cancelled',),
#     'Picked up': ('In Transit', 'Cancelled',),
#     'In Transit': ('Delivered', 'Being processed', 'Cancelled',),
#     'Delivered': ('Cancelled', 'Being processed', 'Cancelled',),
#     'Cancelled': ('Pending', 'Being processed', 'Cancelled',),
# }
#
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'bill00lee@gmail.com' # sendgrid
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'M5a3h8()')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Python ecommerce <bill00lee@gmail.com>'
#
#
#
# import os
#
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
#
# ALLOWED_HOSTS = [
#     '*',
#     '127.0.0.1',
#     'testserver',
#     'localhost',
#                  ]
#
# # Django settings for oscar project.
# PROJECT_DIR = os.path.dirname(__file__)
# location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
#
# DEBUG = True
# TEMPLATE_DEBUG = True
# SQL_DEBUG = True
#
# ADMINS = (
#     # ('Your Name', 'your_email@domain.com'),
# )
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#
# USE_TZ = True
#
# MANAGERS = ADMINS
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'database1',
#         'USER': 'database1_role',
#         'PASSWORD': 'database1_password',
#         'HOST': 'database1',
#         'PORT': '5432',
#         'ATOMIC_REQUESTS': True,
#     }
# }
#
#
# ATOMIC_REQUESTS = True
#
# # Local time zone for this installation. Choices can be found here:
# # http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# # although not all choices may be available on all operating systems.
# # On Unix systems, a value of None will cause Django to use the same
# # timezone as the operating system.
# # If running in a Windows environment this must be set to the same as your
# # system time zone.
# TIME_ZONE = 'America/Toronto'
#
# # Language code for this installation. All choices can be found here:
# # http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGE_CODE = 'en-ca'
#
# gettext_noop = lambda s: s
# LANGUAGES = (
#     ('en-ca', gettext_noop('Canada')),
#     ('zh-cn', gettext_noop('Simplified Chinese')),
#     ('es', gettext_noop('Spanish')),
# )
#
# SITE_ID = 1
#
# # If you set this to False, Django will make some optimizations so as not
# # to load the internationalization machinery.
# USE_I18N = True
#
# # If you set this to False, Django will not format dates, numbers and
# # calendars according to the current locale
# USE_L10N = True
#
# # Absolute path to the directory that holds media.
# # Example: "/home/media/media.lawrence.com/"
# MEDIA_ROOT = location("public/media")
#
# # URL that handles the media served from MEDIA_ROOT. Make sure to use a
# # trailing slash if there is a path component (optional in other cases).
# # Examples: "http://media.lawrence.com", "http://example.com/media/"
# MEDIA_URL = '/media/'
#
# # URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# # trailing slash.
# # Examples: "http://foo.com/media/", "/media/".
# #ADMIN_MEDIA_PREFIX = '/media/admin/'
#
# STATIC_URL = '/static/'
# STATIC_ROOT = location('public')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
#
# # Make this unique, and don't share it with anybody.
# SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p#!)n1a'
#
# MIDDLEWARE = (
#     'django.middleware.locale.LocaleMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
#     'oscar.apps.basket.middleware.BasketMiddleware',
# )
#
#
# ROOT_URLCONF = 'urls'
#
# from oscar import OSCAR_MAIN_TEMPLATE_DIR
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [
#             location('templates'),
#             os.path.join(OSCAR_MAIN_TEMPLATE_DIR, 'templates'),
#             OSCAR_MAIN_TEMPLATE_DIR,
#         ],
#         'OPTIONS': {
#             'loaders': [
#                 'django.template.loaders.filesystem.Loader',
#                 'django.template.loaders.app_directories.Loader',
#             ],
#             'context_processors': [
#                 'django.contrib.auth.context_processors.auth',
#                 'django.template.context_processors.request',
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.i18n',
#                 'django.template.context_processors.media',
#                 'django.template.context_processors.static',
#                 'django.contrib.messages.context_processors.messages',
#
#                 'oscar.apps.search.context_processors.search_form',
#                 'oscar.apps.promotions.context_processors.promotions',
#                 'oscar.apps.checkout.context_processors.checkout',
#                 'oscar.core.context_processors.metadata',
#             ],
#         }
#     }
# ]
#
# # A sample logging configuration. The only tangible logging
# # performed by this configuration is to send an email to
# # the site admins on every HTTP 500 error.
# # See http://docs.djangoproject.com/en/dev/topics/logging for
# # more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'null': {
#             'level': 'DEBUG',
#             'class': 'logging.NullHandler',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'verbose'
#         },
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['null'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': False,
#         },
#         'oscar.checkout': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'INFO',
#         },
#         'django.db.backends': {
#             'handlers': ['null'],
#             'propagate': False,
#             'level': 'DEBUG',
#         },
#         'paypal.express': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#         'paypal.payflow': {
#             'handlers': ['console'],
#             'propagate': True,
#             'level': 'DEBUG',
#         },
#     }
# }
#
# WSGI_APPLICATION = 'frobshop.wsgi.application'
#
#
# from oscar import get_core_apps
# INSTALLED_APPS = [
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.sites',
#     'django.contrib.messages',
#     'django.contrib.admin',
#     'django.contrib.flatpages',
#     'django.contrib.staticfiles',
#     # External apps
#     # 'django_extensions',
#     # 'debug_toolbar',
#     # Apps from oscar
#     # 'paypal',
#     # 'widget_tweaks',
# ]
#
#
# # from oscar import get_core_apps
#
# # INSTALLED_APPS = INSTALLED_APPS + get_core_apps([
#     # 'apps.shipping',
#     # 'apps.order',
#     # 'apps.catalogue',
#     # 'apps.checkout'])
#
# AUTHENTICATION_BACKENDS = (
#     'oscar.apps.customer.auth_backends.EmailBackend',
#     'django.contrib.auth.backends.ModelBackend',
# )
#
# LOGIN_REDIRECT_URL = '/accounts/'
# APPEND_SLASH = True
#
# # Oscar settings
# from oscar.defaults import *
# OSCAR_ALLOW_ANON_CHECKOUT = True
#
# OSCAR_SHOP_TAGLINE = 'PayPal'
#
# # Add Payflow dashboard stuff to settings
# from django.utils.translation import ugettext_lazy as _
# OSCAR_DASHBOARD_NAVIGATION.append(
#     {
#         'label': _('PayPal'),
#         'icon': 'icon-globe',
#         'children': [
#             {
#                 'label': _('PayFlow transactions'),
#                 'url_name': 'paypal-payflow-list',
#             },
#             {
#                 'label': _('Express transactions'),
#                 'url_name': 'paypal-express-list',
#             },
#         ]
#     })
#
#
# # Haystack settings
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }
#
# # Taken from PayPal's documentation - these should always work in the sandbox
# PAYPAL_SANDBOX_MODE = True
# PAYPAL_CALLBACK_HTTPS = False
# PAYPAL_API_VERSION = '119'
#
# # These are the standard PayPal sandbox details from the docs - but I don't
# # think you can get access to the merchant dashboard.
#
#
# PAYPAL_API_USERNAME = 'EelConsultancy-facilitator_api1.gmail.com'
# PAYPAL_API_PASSWORD = '5T2A9NCXZNMBVN2E'
# PAYPAL_API_SIGNATURE = 'A1GGT.a.X8D3d-gBBE6E7iuU2TIeAASCDi8zyqSWdybdQo04FcEsc8g3'
#
#
#
#
# # Standard currency is CAD
# PAYPAL_CURRENCY = PAYPAL_PAYFLOW_CURRENCY = 'CAD'
# PAYPAL_PAYFLOW_DASHBOARD_FORMS = True
#
# # Put your own sandbox settings into an integration.py modulde (that is ignored
# # by git).
# try:
#     from integration import *  # noqa
# except ImportError:
#     pass
#
# OSCAR_INITIAL_ORDER_STATUS = 'Pending'
#
#
# # This dict defines the new order statuses than an order can move to
# OSCAR_ORDER_STATUS_PIPELINE = {
#     'Pending': ('Being processed', 'Cancelled',),
#     'Being processed': ('Complete', 'Cancelled',),
#     'Cancelled': ('Pending', 'Being processed', 'Cancelled',),
#     'Complete': ('Pending', 'Being processed', 'Cancelled',),
# }
#
# # This dict defines the line statuses that will be set when an order's status
# # is changed
# # OSCAR_ORDER_STATUS_CASCADE = {
# #      'Pending': ('Being processed', 'Cancelled',),
# #      'Being processed': ('Complete', 'Cancelled',),
# #      'Complete': 'Cancelled',
# #      'Cancelled': ('Being processed', 'Cancelled',),
# # }
#
# OSCAR_INITIAL_LINE_STATUS = 'Pending'
# OSCAR_LINE_STATUS_PIPELINE = {
#     'Pending': ('Partner Confirmed', 'Cancelled',),
#     'Partner Confirmed': ('Picked up', 'Cancelled',),
#     'Picked up': ('In Transit', 'Cancelled',),
#     'In Transit': ('Delivered', 'Being processed', 'Cancelled',),
#     'Delivered': ('Cancelled', 'Being processed', 'Cancelled',),
#     'Cancelled': ('Pending', 'Being processed', 'Cancelled',),
# }
#
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'bill00lee@gmail.com' # sendgrid
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'M5a3h8()')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Python ecommerce <bill00lee@gmail.com>'
#
#
#
#
# """
# Django settings for frobshop project.
#
# Generated by 'django-admin startproject' using Django 1.11.17.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/1.11/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.11/ref/settings/
# """
# #
# # import os
# # from oscar.defaults import *
# #
# # # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# #
# # BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# #
# # location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)
# #
# # # Quick-start development settings - unsuitable for production
# # # See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
# #
# # # SECURITY WARNING: keep the secret key used in production secret!
# # SECRET_KEY = '(25=)m45g#=tx2nfz=y%y3a_(ya5bj@c_b##c#fz^=5d(y9bje'
# #
# # # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True
# #
# #
# # ALLOWED_HOSTS = [
# #     '*',
# #     '127.0.0.1',
# #     'testserver',
# #     'localhost',
# #                  ]
# #
# #
# # # Application definitions
# #
# # from oscar import get_core_apps
# #
# # INSTALLED_APPS = [
# #     'django.contrib.auth',
# #     'django.contrib.contenttypes',
# #     'django.contrib.sessions',
# #     'django.contrib.sites',
# #     'django.contrib.messages',
# #     'django.contrib.staticfiles',
# #     'django.contrib.flatpages',
# #     # ...
# #     'compressor',
# #     'widget_tweaks',
# # ] + get_core_apps()
# #
# # SITE_ID = 1
# #
# #
# # MIDDLEWARE = (
# #     'django.middleware.locale.LocaleMiddleware',
# #     'django.middleware.common.CommonMiddleware',
# #     'django.contrib.sessions.middleware.SessionMiddleware',
# #     'django.middleware.csrf.CsrfViewMiddleware',
# #     'django.contrib.auth.middleware.AuthenticationMiddleware',
# #     'django.contrib.messages.middleware.MessageMiddleware',
# #     'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
# #     # 'debug_toolbar.middleware.DebugToolbarMiddleware',
# #     'oscar.apps.basket.middleware.BasketMiddleware',
# # )
# #
# # ROOT_URLCONF = 'frobshop.urls'
# #
# # from oscar import OSCAR_MAIN_TEMPLATE_DIR
# #
# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #
# #         'DIRS': [
# #                     location('templates'), # templates directory of the project
# #                 ],
# #
# #
# #         # 'DIRS': [
# #         #     os.path.join(BASE_DIR, 'templates'),
# #         #     OSCAR_MAIN_TEMPLATE_DIR
# #         # ],
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.debug',
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.template.context_processors.i18n',
# #                 'django.contrib.messages.context_processors.messages',
# #
# #                 'oscar.apps.search.context_processors.search_form',
# #                 'oscar.apps.promotions.context_processors.promotions',
# #                 'oscar.apps.checkout.context_processors.checkout',
# #                 'oscar.apps.customer.notifications.context_processors.notifications',
# #                 'oscar.core.context_processors.metadata',
# #             ],
# #         },
# #     },
# # ]
# #
# # WSGI_APPLICATION = 'frobshop.wsgi.application'
# #
# #
# # # Database
# # # https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# #
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
# #         'NAME': 'database1',
# #         'USER': 'database1_role',
# #         'PASSWORD': 'database1_password',
# #         'HOST': 'database1',
# #         'PORT': '5432',
# #         'ATOMIC_REQUESTS': True,
# #     }
# # }
# #
# #
# # # Haystack settings
# # HAYSTACK_CONNECTIONS = {
# #     'default': {
# #         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
# #     },
# # }
# #
# #
# # # Password validation
# # # https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
# #
# # AUTH_PASSWORD_VALIDATORS = [
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
# #     },
# #     {
# #         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
# #     },
# # ]
# #
# # AUTHENTICATION_BACKENDS = (
# #     'oscar.apps.customer.auth_backends.EmailBackend',
# #     'django.contrib.auth.backends.ModelBackend',
# # )
# #
# # OSCAR_ALLOW_ANON_CHECKOUT = True
# # # Internationalization
# # # https://docs.djangoproject.com/en/1.11/topics/i18n/
# #
# # LANGUAGE_CODE = 'en-ca'
# #
# # gettext_noop = lambda s: s
# # LANGUAGES = (
# #     ('en-ca', gettext_noop('Canada')),
# #     ('zh-cn', gettext_noop('Simplified Chinese')),
# #     ('es', gettext_noop('Spanish')),
# # )
# #
# #
# # TIME_ZONE = 'UTC'
# #
# # USE_I18N = True
# #
# # USE_L10N = True
# #
# # USE_TZ = True
# #
# #
# # # Static files (CSS, JavaScript, Images)
# # # https://docs.djangoproject.com/en/1.11/howto/static-files/
# #
# # # Static files (CSS, JavaScript, Images)
# # # https://docs.djangoproject.com/en/2.1/howto/static-files/
# # STATIC_URL = '/static/'
# #
# # STATICFILES_DIRS = [
# #     os.path.join(BASE_DIR, "static"),
# # ]
# #
# # STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "static_root")
# #
# #
# # MEDIA_URL = '/media/'
# # MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "media_root")
# #
# #
# # PROTECTED_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn", "protected_media")
# #
# #
# #
# # OSCAR_INITIAL_ORDER_STATUS = 'Pending'
# # OSCAR_INITIAL_LINE_STATUS = 'Pending'
# # OSCAR_ORDER_STATUS_PIPELINE = {
# #     'Pending': ('Being processed', 'Cancelled',),
# #     'Being processed': ('Processed', 'Cancelled',),
# #     'Cancelled': (),
# # }