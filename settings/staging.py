from base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal environment variables
SITE_URL = 'starbex.herokuapp.com'
PAYPAL_NOTIFY_URL = 'starbex.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'rebm01-facilitator@hotmail.co.uk'
