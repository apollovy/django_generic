'''
Created on 08.08.2012

@author: apollov
'''
from django.utils.translation import ugettext_lazy as _

from django.contrib.admin.options import ModelAdmin

from helpers import admin, inline, with_section, file_url_fabric

_titled_dict = dict(
    fieldsets=(
        (None, {'fields': ('title',)}),
    ),
    list_display=('title',),
    search_fields=('title',),
)

TitledAdmin = admin('TitledAdmin', _titled_dict)
TitledInline = inline('TitledInline', _titled_dict)

with_title = with_section(TitledAdmin)
with_title_inline = with_section(TitledInline)


_metafielded_dict = dict(
    fieldsets=(
        (_('Meta properties'), {
            'fields': ('meta_title', 'meta_description', 'meta_keywords',),
            'classes': ('collapse',),
    }),),
    search_fields=('meta_title', 'meta_description', 'meta_keywords',),
)

MetaFieldedAdmin = admin('MetaFieldedAdmin', _metafielded_dict)
MetaFieldedInline = inline('MetaFieldedAdmin', _metafielded_dict)

with_metafields = with_section(MetaFieldedAdmin)
with_metafields_inline = with_section(MetaFieldedInline)


_sortable_dict = dict(
    fieldsets=(
        (None, {'fields': ('sorting_order',)}),
    ),
    list_display=('sorting_order',),
)

SortableAdmin = admin('SortableAdmin', _sortable_dict)
SortableInline = inline('SortableInline', _sortable_dict)

with_sorting = with_section(SortableAdmin)
with_sorting_inline = with_section(SortableInline)


_fileable_dict = dict(
    fieldsets=(
        (None, {'fields': ('file',)}),
    ),
    list_display=('file_url',),
    file_url=file_url_fabric('file'),
)

FileableAdmin = admin('FileableAdmin', _fileable_dict)
FileableInline = inline('FileableInline', _fileable_dict)

with_file = with_section(FileableAdmin)
with_file_inline = with_section(FileableInline)


_imageable_dict = dict(
    fieldsets=(
        (None, {'fields': ('image',)}),
    ),
    list_display=('file_url',),
    file_url=file_url_fabric('image'),
)

ImageableAdmin = admin('ImageableAdmin', _imageable_dict)
ImageableInline = inline('ImageableInline', _imageable_dict)

with_image = with_section(ImageableAdmin)
with_image_inline = with_section(ImageableInline)


_descripted_dict = dict(
    fieldsets=(
        (None, {'fields': ('description',)}),
    ),
    search_fields=('description',),
)

DescriptedAdmin = admin('DescriptedAdmin', _descripted_dict)
DescriptedInline = inline('DescriptedInline', _descripted_dict)

with_description = with_section(DescriptedAdmin)
with_description_inline = with_section(DescriptedInline)


def _publish_wrapper(func_name, publish):
    def wrapper(modeladmin, request, queryset):
        queryset.update(is_published=publish)
    wrapper.func_name = func_name
    return wrapper


_make_published = _publish_wrapper('make_published', True)
_make_published.short_description = _('Publish selected items')

_make_unpublished = _publish_wrapper('make_unpublished', False)
_make_unpublished.short_description = _('Unpublish selected items')

_published_dict = dict(
    fieldsets=(
        (None, {'fields': (('is_published', 'publish_date_time'),)}),
    ),
    date_hierarchy='publish_date_time',
    list_display=('publish_date_time', 'is_published',),
    list_editable=('is_published',),
    list_filter=('is_published',),
    actions=(_make_published, _make_unpublished,),
)

PublishedAdmin = admin('PublishedAdmin', _published_dict)
PublishedInline = inline('PublishedInline', _published_dict)

with_published = with_section(PublishedAdmin)
with_published_inline = with_section(PublishedInline)


@with_published
@with_sorting
@with_title
class TitledSortablePublishedAdmin(ModelAdmin):
    pass
