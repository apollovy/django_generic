#!/usr/bin/env python

from setuptools import setup, find_packages

from apollov import get_version
from apollov.django.apps.generic import VERSION


setup(name='django-generic',
    version=get_version(VERSION).replace(' ', '-'),
    description='Generic models app for django',
    author='Yuriy A. Apollov',
    author_email='apollovy@gmail.com',
    license='BSD',
    platforms=['any',],
    url='http://github.com/apollovy/django-generic',
    include_package_data = True,
    zip_safe=False,
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
