'''
Created on 04.12.2012

@author: apollov
'''
from os.path import splitext as _splitext, basename as _basename

from django import template

register = template.Library()


@register.filter
def splitext(value):
    return _splitext(value)


@register.filter
def basename(value):
    return _basename(value)
