'''
Created on 14.11.2012

@author: apollov
'''
from datetime import datetime

from django.db.models import Manager


class PublishedManager(Manager):
    def published(self):
        return self.get_query_set().filter(
           is_published=True,
           publish_date_time__lte=datetime.now(),
       )

    def published_future(self):
        return self.get_query_set().filter(
           is_published=True,
           publish_date_time__gt=datetime.now(),
       )
