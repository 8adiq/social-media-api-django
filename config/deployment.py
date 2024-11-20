import os
from .settings import *
from .settings import BASE_DIR


ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME','social-media-api-bsfmbnbbh4g6hvfy.southafricanorth-01.azurewebsites.net')]
CSRF_TRUSTED_ORIGINS = ['https:/'+ os.environ.get('WEBSITE_HOSTNAME','social-media-api-bsfmbnbbh4g6hvfy.southafricanorth-01.azurewebsites.net')]
DEBUG=False
SECRET_KEY = os.environ['SECRET']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


STATICFILEs_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

connectionstring = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
parameters = {pair.split('='):pair.split('=') for pair in connectionstring.split(' ')}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': parameters['dbname'], 
        'USER': parameters['user'], 
        'PASSWORD': parameters['password'],   
        'HOST': parameters['host'],           
        # 'PORT': parameters['port'],    
    }
}

