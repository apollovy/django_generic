'''
Created on 08.11.2012

@author: apollov
'''
from django.utils.translation import get_language

import haystack.query
import haystack.models


class MlSearchResult(haystack.models.SearchResult):
    @property
    def text(self):
        return getattr(self, "text_%s" % str(get_language()))


class MlSearchQuerySet(haystack.query.SearchQuerySet):
    def __init__(self, site=None, query=None):
        haystack.query.SearchQuerySet.__init__(self, site=site, query=query)
        self.query.set_result_class(MlSearchResult)

    def filter(self, **kwargs):
        """
        Narrows the search based on certain attributes and the default
         operator.
        """
        if 'content' in kwargs:
            kwd = kwargs.pop('content')
            kwdkey = "text_%s" % str(get_language())
            kwargs[kwdkey] = kwd
        return super(MlSearchQuerySet, self).filter(**kwargs)
