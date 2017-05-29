from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CLEAR_DB_URL = os.environ.get("CLEARDB_DATABASE_URL", "")

DATABASES['default'] = dj_database_url.parse(CLEAR_DB_URL)

SITE_URL = 'starbex.herokuapp.com'

# Paypal environment variables
PAYPAL_NOTIFY_URL = 'starbex.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'rebm01-facilitator1@hotmail.co.uk'
