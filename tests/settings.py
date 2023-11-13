# settings_dev.py

import django
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f"BASE_DIR={BASE_DIR}")

DEBUG = True
SECRET_KEY = 'fake-key'
ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django_live_log',
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.CommonMiddleware",
]

import os
PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_ROOT, "templates"), ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ]
        },
    },
]

database_engine = os.environ.get("DATABASE_ENGINE", "sqlite")
database_config = {
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'admin_interface',
    #     'USER': 'mysql',
    #     'PASSWORD': 'mysql',
    #     'HOST': '',
    #     'PORT': '',
    # },
    # "postgres": {
    #     "ENGINE": "django.db.backends.postgresql_psycopg2",
    #     "NAME": "admin_interface",
    #     "USER": "postgres",
    #     "PASSWORD": "postgres",
    #     "HOST": "",
    #     "PORT": "",
    # },
}

DATABASES = {
    "default": database_config.get(database_engine),
}

USE_TZ = True
ROOT_URLCONF = "django_live_log.urls"

#--------------------------------
DLL_FILE = "/tmp/django_live_log.log"
