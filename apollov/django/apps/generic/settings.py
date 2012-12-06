'''
Created on 28.11.2012

@author: apollov
'''
from django.conf import settings

GENERIC_SETTINGS = {
    'TITLE_MAX_LENGTH': 200,
    'MAX_EMAIL_LENGTH': 320,  # http://tools.ietf.org/html/rfc3696#section-3
}

GENERIC_SETTINGS.update(getattr(settings, 'GENERIC_SETTINGS', {}))
