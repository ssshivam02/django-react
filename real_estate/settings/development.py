from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = 'info@shivamreal_estate.com'
DOMAIN = env('DOMAIN')
SITE_NAME = 'Real Estate'

DATABASES = {
        'default': {
            'ENGINE': env("POSTGRES_ENGINE"),
            'NAME': env("POSTGRES_NAME"),
            'USER': env("POSTGRES_USER"),
            'PASSWORD': env("POSTGRES_PASSWORD"),
            'HOST': env("POSTGRES_HOST"),
            'PORT': env("POSTGRES_PORT"),
        }
}
