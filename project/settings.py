import os
from environs import Env


env = Env()
env.read_env()
DATABASES = {
    'default': {
        'ENGINE': env("ENGINE_BSC"),
        'HOST': env("HOST_BSC"),
        'PORT': env("PORT_BSC"),
        'NAME': env("NAME_BSC"),
        'USER': env("USER_BSC"),
        'PASSWORD': env("PASSWORD_BSC"),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY_BSC")

DEBUG = env.bool("DEBUG_BSC")

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
