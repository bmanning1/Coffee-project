from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
DATABASES['default'] = dj_database_url.config("mysql://b4e94acd0b2f51:eb48feb4@eu-cdbr-west-01.cleardb.com/heroku_cc39facad1a3501?")

# Paypal environment variables
SITE_URL = 'starbex.herokuapp.com'
PAYPAL_NOTIFY_URL = 'starbex.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'rebm01-facilitator@hotmail.co.uk'
