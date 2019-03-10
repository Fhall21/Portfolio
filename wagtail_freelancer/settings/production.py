import os

from .base import *
from decouple import config

env = os.environ.copy()

DEBUG = config('DEBUG', True, cast=bool)

SECRET_KEY = config('SECRET_KEY')

#ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

try:
    from .local import *
except ImportError:
    pass

