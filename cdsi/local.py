# Email settings
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True

SITE_COMPANY_NAME = 'Gonzales Family Dental Care'
EMAIL_CONTACTUS_SUBJECT = 'An message from ' + SITE_COMPANY_NAME
EMAIL_APPOINTMENT_SUBJECT = 'An appointment request from ' + SITE_COMPANY_NAME + ' Website'
EMAIL_SIGNATURE = 'Sincerely, ' + SITE_COMPANY_NAME + ' Website Messenger'
EMAIL_TO = 'pobrejuanito@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ki@audioverse.org'
EMAIL_HOST_PASSWORD = 'H0lyPl@ce10221844'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    BASE_DIR + '/static',
)
