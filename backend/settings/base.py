from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'your-secret-key'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # other installed apps...
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # other middleware...
]

# Other common settings...
