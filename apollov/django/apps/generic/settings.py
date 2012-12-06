'''
Created on 28.11.2012

@author: apollov
'''
from django.conf import settings

GENERIC_SETTINGS = {
    'EMAIL_LENGTH_MAX': 320,  # http://tools.ietf.org/html/rfc3696#section-3
    'NAME_LENGTH_MAX': 100,
    'TITLE_LENGTH_MAX': 200,
}

GENERIC_SETTINGS.update(getattr(settings, 'GENERIC_SETTINGS', {}))
