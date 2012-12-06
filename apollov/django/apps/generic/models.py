'''
Created on 07.08.2012

@author: apollov
'''
from datetime import datetime

from django.db.models import (Model, CharField, SmallIntegerField, ImageField,
    TextField, FileField, DateTimeField, BooleanField, EmailField,)
from django.utils.translation import ugettext_lazy as _

from helpers import file_like_function_fabric
from managers import PublishedManager
from settings import GENERIC_SETTINGS


class Titled(Model):
    '''
    Abstract model with title.
    '''
    title = CharField(
        max_length=GENERIC_SETTINGS['TITLE_MAX_LENGTH'],
        verbose_name=_('title'),
    )

    class Meta(object):
        abstract = True

    def __unicode__(self):
        return u'%s' % self.title


class Sortable(Model):
    '''
    Abstract model with sorting order.
    '''
    sorting_order = SmallIntegerField(
        verbose_name=_('sorting order'),
        default=0,
    )

    class Meta(object):
        abstract = True
        ordering = ['sorting_order', ]


class MetaFielded(Model):
    '''
    Abstract model with fields responsible for meta tags on a web page.
    '''
    meta_title = CharField(
        max_length=GENERIC_SETTINGS['TITLE_MAX_LENGTH'],
        verbose_name=_('meta title'),
        null=True,
        blank=True,
    )
    meta_description = CharField(
        max_length=GENERIC_SETTINGS['TITLE_MAX_LENGTH'],
        verbose_name=_('meta description'),
        null=True,
        blank=True,
    )
    meta_keywords = CharField(
        max_length=GENERIC_SETTINGS['TITLE_MAX_LENGTH'],
        verbose_name=_('meta keywords'),
        null=True,
        blank=True,
    )

    class Meta(object):
        abstract = True


def ImageableModelFabric(*args, **kwargs):
    '''
    @usage: ImageableModelFabric(__file__, model_name)
    '''
    return file_like_function_fabric(ImageField, 'image')(*args, **kwargs)


def FileableModelFabric(*args, **kwargs):
    '''
    @usage: FileableModelFabric(__file__, model_name)
    '''
    return file_like_function_fabric(FileField, 'file')(*args, **kwargs)


class Descripted(Model):
    description = TextField(
        verbose_name=_('description'),
        null=True,
        blank=True,
    )

    class Meta(object):
        abstract = True


class Published(Model):
    publish_date_time = DateTimeField(
        verbose_name=_('publish date and time'),
        null=True,
        blank=True,
        default=datetime.now,
    )
    is_published = BooleanField(
        verbose_name=_('published?'),
        null=False,
        blank=False,
    )

    class Meta(object):
        abstract = True

    objects = PublishedManager()

    @classmethod
    def publish_date_set(cls):
        fname = 'publish_date_time'
        return set(i[fname].date() for i in cls.objects.published()\
                   .order_by(fname).values(fname))


class Emailed(Model):
    email = EmailField(
        max_length=GENERIC_SETTINGS['MAX_EMAIL_LENGTH'],
        verbose_name=_('email'),
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class TitledSortablePublished(Titled, Sortable, Published):
    class Meta(Sortable.Meta):
        abstract = True
