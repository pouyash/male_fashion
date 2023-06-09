from pathlib import Path
from . import local_settings as LS
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!qhp=sp!=gz*0&dg-m6r@eohjbe45ik+&qdtf8_kd4@^w7m-lk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # EXTERNAL APPS
    'django_render_partial',
    'sweetify',
    'captcha',
    'ckeditor',
    'ckeditor_uploader',

    # 'easy_thumbnails',
    # 'filer',
    # 'mptt',

    #INTERNAL APPS
    'site_settings',
    'home',
    'product',
    'user',
    'blog',
    'contact',
    'about',
    'order',
    'polls',
    'account',
]

# Filer
FILER_CANONICAL_URL = 'sharing/'


# CKEditor Settings
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
# CKEDITOR_FILENAME_GENERATOR = BASE_DIR / 'utils/utils.get_filename'
CKEDITOR_ALLOW_NONIMAGE_FILES = False

CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}

LOGIN_URL = '/user/login/'

########   Send Email Configuration From Mailtrap    ****************************

EMAIL_HOST = LS.EMAIL_HOST
EMAIL_HOST_USER = LS.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = LS.EMAIL_HOST_PASSWORD
EMAIL_PORT = LS.EMAIL_PORT


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fasion_male.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'fasion_male.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

AUTH_USER_MODEL = 'user.User'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': LS.DB_NAME,
        'HOST': LS.DB_HOST,
        'USER': LS.DB_USER,
        'PASSWORD': LS.DB_PASSWORD,
        'PORT': LS.DB_PORT,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
# STATICFILES_DIRS = [
#     BASE_DIR / 'static'
# ]

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR/'media'
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
