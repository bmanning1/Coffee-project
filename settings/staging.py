from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
    }
}

DATABASES['default'] = dj_database_url.config("mysql://b4e94acd0b2f51:eb48feb4@eu-cdbr-west-01.cleardb.com/heroku_cc39facad1a3501?")

SITE_URL = 'starbex.herokuapp.com'

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'starbex.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'rebm01-facilitator@hotmail.co.uk'
