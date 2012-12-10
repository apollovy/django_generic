'''
Created on 10.12.2012

@author: apollov
'''
import datetime

from haystack import indexes


class TranslationSearchIndexMixin(indexes.SearchIndex):
    text_ru = indexes.CharField(document=True, use_template=True)
    text_en = indexes.CharField(use_template=True)


class PublishedSearchIndexMixin(indexes.SearchIndex):
    publish_date_time = indexes.DateTimeField(model_attr='publish_date_time')
    is_published = indexes.BooleanField(model_attr='is_published')

    def read_queryset(self):
        return super(PublishedSearchIndexMixin, self).index_queryset()\
            .filter(publish_date_time__lte=datetime.datetime.now(),
                    is_published=True)
