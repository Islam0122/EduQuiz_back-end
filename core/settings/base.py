import os
from datetime import timedelta
from pathlib import Path
from django.utils import timezone
from .env_reader import env


SECRET_KEY = env('SECRET_KEY')

BASE_DIR = Path(__file__).resolve().parent.parent

PRODUCTION = True


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'corsheaders',
    'drf_yasg',
    'debug_toolbar',

    # > apps <
    'app.quiz'

]
# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Добавьте сюда
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # должен быть до CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True


USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath("static")

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from .cors import *

if not PRODUCTION:
    from .local import *
else:
    from .prod import *

# if DEBUG:
#     INTERNAL_IPS = ['127.0.0.1','localhost',]
#     MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]


