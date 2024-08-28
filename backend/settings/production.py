from .base import *

DEBUG = False

ALLOWED_HOSTS = ['totsworld.co.in','api.totsworld.co.in']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': 'your_db_port',
    }
}

# Other production-specific settings...
