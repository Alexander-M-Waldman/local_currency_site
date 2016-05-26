"""
Django settings for geodjango project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os, sys

# import django
# django.setup()
sys.path.append("/opt/venv/lib/python2.7/site-packages")


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print BASE_DIR


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(dxnf(^&v+0eqhcytf(##0(^hpag_ack6+#ornu-7#2_o=557z'
#from django.utils.crypto import get_random_string
# chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
# SECRET_KEY = get_random_string(50, chars)
# print SECRET_KEY
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    #'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'world',
    'crispy_forms',
    'debug_toolbar',
    #'userena',
    #'guardian',
    #'easy_thumbnails',
    #'accounts',
    #'django.contrib.formtools',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    #'userena.middleware.UserenaLocaleMiddleware',
]

ROOT_URLCONF = 'geodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR , 'geodjango/static/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = 'geodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'geodjango',
        'HOST': 'localhost',
        'USER': 'user',
        'PASSWORD': 'password',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = (
    #'userena.backends.UserenaAuthenticationBackend',
    #'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

if DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR , "geodjango", "static", "static-only")
    MEDIA_ROOT = os.path.join(BASE_DIR, "geodjango", "static", "media")
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "geodjango", "static", "static"),
        )

#crispy form tags settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#Django registration redux settings
#ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
#REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.


#ANONYMOUS_USER_ID = -1
#SITE_ID=2

#AUTH_PROFILE_MODULE = 'accounts.MyProfile'

#LOGIN_REDIRECT_URL = '/accounts/%(username)s/' 
#LOGIN_URL = '/accounts/signin/'
#LOGOUT_URL = '/accounts/signout/'

#USERENA_DISABLE_SIGNUP = False
#USERENA_ACTIVATION_REQUIRED = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'hostemail@email.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_PORT = 587

def show_toolbar(request):
    if not request.is_ajax() and request.user and request.user.username == "admin":
        return True
    return False

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'geodjango.settings.show_toolbar',
}