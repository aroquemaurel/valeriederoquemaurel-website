from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         # Backends disponibles : 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
         'NAME': 'valerie_v3',
         'USER': 'valerie_v3',
         'PASSWORD': 'OUFf7yKZ8AKSuuTq',
         'HOST': '127.0.0.1',
         'PORT': '',
         'OPTIONS': {
             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
         },
     }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s - %(asctime)s %(filename)s:%(lineno)s - function %(funcName)s\n*******\t%(message)s'
        },
    },
    'handlers': {
        'file_info': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 10,  # keep at most 10 log files
            'maxBytes': 5242880,  # 5*1024*1024 bytes (5MB)
            'filename': os.path.join(BASE_DIR, 'logs/valerie_info.log'),
            'formatter': 'verbose'
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 10,  # keep at most 10 log files
            'maxBytes': 5242880,  # 5*1024*1024 bytes (5MB)
            'filename': os.path.join(BASE_DIR, 'logs/valerie_debug.log'),
            'formatter': 'verbose',
        },
        'file_errors': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'backupCount': 10,  # keep at most 10 log files
            'maxBytes': 5242880,  # 5*1024*1024 bytes (5MB)
            'filename': os.path.join(BASE_DIR, 'logs/valerie_errors.log'),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file_debug', 'file_errors', 'file_info'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
