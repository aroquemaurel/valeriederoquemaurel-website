from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         # Backends disponibles : 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'ci',
         'USER': 'root',
         'PASSWORD': 'mysql_password_ci',
         'HOST': 'mysql',
         'PORT': '',
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
         },
     }
}
