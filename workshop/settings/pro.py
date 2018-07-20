from .base import *

DEBUG = True

ADMINS = (
    ('Ivan', 'info@poly-edr.ru'),
)

ALLOWED_HOSTS = ['.zo-0.ru', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'awesome_db',
        'USER': 'awesome_user',
        'PASSWORD': 'awesome_password',   
        
        
    }
}
