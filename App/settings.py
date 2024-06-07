"""
Django settings for App project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tpq^-r#u-%fu4fd936f!0zf^uvk@6)208c5d_eu#zz^d7=**8w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']
CORS_ALLOWED_ORIGINS = [
        "http://localhost:4000",
        "http://localhost:5000",
        "http://localhost:3000",
        "http://localhost:3001",
       
]
CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
)

CORS_ALLOW_HEADERS = [
    'access-control-allow-origin',
    'access_token',
    'accept',
    'CORS_ALLOWED_ORIGINS'
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'language',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework_simplejwt.token_blacklist',
    "rest_framework",
    'corsheaders',
    'django_rest_passwordreset',
    "rest_framework_simplejwt",
    "sarox",
    "d11_point_prediction",
    "mongo",
]
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
          # Replace with your actual authentication class
    ],
}
from datetime import datetime, timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}




SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'email',  # Replace with the actual field used as the user identifier
    'USER_ID_CLAIM': 'email',  # Replace with the actual claim for the user identifier
}
MIDDLEWARE = [
    
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    
 
]

ROOT_URLCONF = "App.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "App.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
# from mongoengine import connect

# # Connect to MongoDB
# connect(
#     db='admin',
#     host='mongodb://localhost:27017/admin'
# )

# DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'NAME': 'Amit',
#         # 'ENFORCE_SCHEMA': False,  # Optionally set this to True if you want to enforce schema validation
#         'CLIENT': {
#             'host': 'mongodb://localhost:27017',
#             # Other client options such as username, password, etc.
#         }
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'saroxdb',
#         'USER': 'saroxuser',
#         'PASSWORD': 'sarox_user123',
#         'HOST': '18.189.18.223',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # or your SMTP server's port
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = 'amitraazec53@gmail.com'
EMAIL_HOST_PASSWORD = 'jurm sklb gpnx rncb'

# import os
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



# settings.py

# AWS_ACCESS_KEY_ID = 'AKIAW3MEAYO4JQ4IWQPV'
# AWS_SECRET_ACCESS_KEY = 'UuCJbU3/jXuCKNJ2GejY6vrtpDWrKYDts3Ip/9mJ'
# AWS_STORAGE_BUCKET_NAME = 'progrowth-project-v1'
# AWS_DEFAULT_ACL = 'private'
# AWS_S3_REGION_NAME = 'ap-south-1'  # e.g., us-west-2

# AWS_S3_VERIFY = True
# AWS_S3_FILE_OVERWRITE = False
# DEFAULT_FILE_STORAGE= 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_FILE_OVERWRITE = False


# settings.py

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'reset_google_form_links_task': {
        'task': 'your_app_name.tasks.reset_google_form_links_task',
        'schedule': crontab(minute=0, hour=0),  # Run daily at midnight
    },
}
