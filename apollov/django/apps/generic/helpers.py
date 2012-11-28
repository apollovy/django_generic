'''
Created on 28.11.2012

@author: apollov
'''
from posixpath import join, sep, splitext

from django.db.models import Model
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import capfirst

from django.contrib.admin.options import ModelAdmin, InlineModelAdmin


def module_dict(**kwargs):
    kwargs.update(__module__='apollov.django.apps.generic.admin')
    return kwargs


def file_url_fabric(attr_name):
    def wrapper(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (
            getattr(obj, attr_name).url, capfirst(_('link')),)
    wrapper.short_description = _(attr_name)
    wrapper.allow_tags = True
    return wrapper


def with_section(model_admin):
    def wrapper(cls):
        def _handle_attr(attr_name, default_value=None):
            def wrapper(cls):
                cls_attr = getattr(cls, attr_name, default_value)
                model_admin_attr = getattr(model_admin, attr_name,
                                           default_value)
                if model_admin_attr != default_value and model_admin_attr:
                    if cls_attr != default_value and cls_attr:
                        setattr(cls, attr_name, cls_attr + model_admin_attr)
                    else:
                        setattr(cls, attr_name, model_admin_attr)
                return cls
            return wrapper
        for handler in (
            _handle_attr('fieldsets'),
            _handle_attr('date_hierarchy'),
            _handle_attr('list_display', ('__str__',)),
            _handle_attr('list_display_links'),
            _handle_attr('list_editable'),
            _handle_attr('list_filter'),
        ):
            cls = handler(cls)
        return type(cls.__name__, (cls, model_admin), module_dict())
    return wrapper


def admin(name, _dict):
    return type(name, (ModelAdmin,), module_dict(**_dict))


def inline(name, _dict):
    return type(name, (InlineModelAdmin,), module_dict(**_dict))


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
