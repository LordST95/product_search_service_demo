from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret! ==> sure, I will do ;)
SECRET_KEY = 'django-insecure-uax3do3sxnpl0frr(@*nbmz^)t*lh%kbo#t@$#s(23bo1f^d@7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # djangorestframework
    'rest_framework',
    # djangorestframework-simplejwt
    'rest_framework_simplejwt',
    # django-filter
    'django_filters',
    # django-cors-headers
    'corsheaders',
    # django_extensions (shell_plus)
    'django_extensions',
    # drf-yasg
    'drf_yasg',
    # django-imagekit
    'imagekit',
    
    # My Apps
    'accounts',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_search_db',
        'USER': 'root',
        'PASSWORD': 'fake_pass',
        'HOST': 'db',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
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

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.Member'

MAIN_ADMIN_F_NAME = "Test"
MAIN_ADMIN_L_NAME = "Tester"
MAIN_ADMIN_USER = "test"
MAIN_ADMIN_PASS = "test"
MAIN_ADMIN_EMAIL = "sina.tamjidy@gmail.com"     # not real one :)

AUTH_PASSWORD_VALIDATORS = []

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),
}

# CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'      # TODO, later, set it based on .env
CELERY_BROKER_URL = 'redis://redis:6379/1'      # TODO, later, set it based on .env
CELERY_BROKER_TRANSPORT_OPTIONS = {"max_retries": 1, "interval_start": 0, "interval_step": 0.2, "interval_max": 0.2}

MEDIA_ROOT = BASE_DIR.joinpath("media_server_folder")
MEDIA_URL = '/media/'




EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = 'sina@gmail.com'
EMAIL_HOST_PASSWORD = 'fakePass2023$'
EMAIL_PORT = 2525
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   # we can didn't write it
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"
