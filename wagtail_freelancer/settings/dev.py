from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#STATIC_URL = '/static/'

#MEDIA_URL = '/media/'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1&3rqr_6=x*qn93mwg=ao2d(lm9od&q67xi1gayz9wuf9867t#'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*', 'felix-hall.com', '127.0.0.1', '138.68.255.50'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
