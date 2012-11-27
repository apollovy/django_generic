'''
Created on 07.08.2012

@author: apollov
'''
from posixpath import join, sep, splitext
from datetime import datetime

from django.db.models import (Model, CharField, SmallIntegerField, ImageField,
    TextField, FileField, DateTimeField, BooleanField)
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from managers import PublishedManager


class Titled(Model):
    '''
    Abstract model with title.
    '''
    title = CharField(
        max_length=settings.TITLE_MAX_LENGTH,
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
        max_length=settings.TITLE_MAX_LENGTH,
        verbose_name=_('meta title'),
        null=True,
        blank=True,
    )
    meta_description = CharField(
        max_length=settings.TITLE_MAX_LENGTH,
        verbose_name=_('meta description'),
        null=True,
        blank=True,
    )
    meta_keywords = CharField(
        max_length=settings.TITLE_MAX_LENGTH,
        verbose_name=_('meta keywords'),
        null=True,
        blank=True,
    )

    class Meta(object):
        abstract = True


def upload_to(file_name, model_name, *args):
    return join(settings.PROJECT_NAME,
                splitext(file_name.split(sep)[-2])[0],
                model_name,
                *args)


def file_like_function_fabric(field_class, _property_name):
    '''
    @usage: Fabric(__file__, model_name)
    '''
    def Wrapper(file_name, model_name, property_name=_property_name,
                null=False, blank=False,):
        im_dict = {
            property_name: field_class(
                upload_to=upload_to(file_name, model_name, property_name),
                verbose_name=_(property_name.replace('_', ' ')),
                null=null,
                blank=blank,
            ),
            'Meta': type('Meta', (object,), {'abstract': True, }),
            '__module__': 'apollov.django.apps.generic.models',
        }

        return type('%sable' % field_class.__name__.replace('Field', ''),
                    (Model,), im_dict)
    return Wrapper


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


class TitledSortablePublished(Titled, Sortable, Published):
    class Meta(Sortable.Meta):
        abstract = True
