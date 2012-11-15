'''
Created on 08.08.2012

@author: apollov
'''
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin import ModelAdmin


def with_section(model_admin, to_top=False):
    def wrapper(cls):
        if cls.fieldsets:
            if not to_top:
                cls.fieldsets = cls.fieldsets + model_admin.fieldsets
            else:
                cls.fieldsets = model_admin.fieldsets + cls.fieldsets
        else:
            cls.fieldsets = model_admin.fieldsets
        return cls
    return wrapper


class TitledAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('title',)}),
    )

with_title = with_section(TitledAdmin)


class MetaFieldedAdmin(ModelAdmin):
    fieldsets = (
        (_('Meta properties'), {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',),
    }),)

with_metafields = with_section(MetaFieldedAdmin)


class SortableAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('sorting_order',)}),
    )

with_sorting = with_section(SortableAdmin)


class FileableAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('file',)}),
    )

with_file = with_section(FileableAdmin)


class ImageableAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('image',)}),
    )

with_image = with_section(ImageableAdmin)


class DescriptedAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('description',)}),
    )

with_description = with_section(DescriptedAdmin)


class PublishedAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': (('is_published', 'publish_date_time'),)}),
    )

with_published = with_section(PublishedAdmin)


@with_published
@with_sorting
@with_title
class TitledSortablePublishedAdmin(ModelAdmin):
    list_display = ('sorting_order', 'title', 'is_published',)
    list_display_links = ('title',)
    list_editable = ('sorting_order', 'is_published',)
    list_filter = ('is_published',)
