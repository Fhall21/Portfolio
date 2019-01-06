import os

from .base import *

env = os.environ.copy()

DEBUG = False

SECRET_KEY = env['SECRET_KEY']

#ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

try:
    from .local import *
except ImportError:
    pass



AWS_ACCESS_KEY_ID = 'AKIAI2YLK5C66Z5I6ONA'
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'personal-portfolio-bucket'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

AWS_STATIC_LOCATION = 'static'
STATICFILES_STORAGE = 'wagtail_freelancer.storage_backends.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)

AWS_PUBLIC_MEDIA_LOCATION = 'media/public'
DEFAULT_FILE_STORAGE = 'wagtail_freelancer.storage_backends.PublicMediaStorage'

AWS_PRIVATE_MEDIA_LOCATION = 'media/private'
PRIVATE_FILE_STORAGE = 'wagtail_freelancer.storage_backends.PrivateMediaStorage'
'''