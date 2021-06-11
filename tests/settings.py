import os.path


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'django_cute_status')

SECRET_KEY = 'ThisIsNotASecretKey'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['django_cute_status']

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3'}}

USE_TZ = True

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
    ],
}]

ROOT_URLCONF = 'tests.urls'

MIDDLEWARE = ['django_cute_status.middleware.CuteStatusMiddleware']
