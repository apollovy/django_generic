'''
Created on 14.11.2012

@author: apollov
'''
from django.db.models import Manager


class PublishedManager(Manager):
    def published(self):
        return self.get_query_set().filter(is_published=True)
