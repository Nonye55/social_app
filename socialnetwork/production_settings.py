from .development_settings import *

SECRET_KEY = env.str('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']

DATABASES = {
    'default': env.db('DATABASE_URL')
}
