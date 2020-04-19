from .base import *
import os
from decouple import config
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG',  default=True, cast=bool)
ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
