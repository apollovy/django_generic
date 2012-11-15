'''
Created on 14.09.2012

@author: apollov
'''
from modeltranslation.translator import TranslationOptions


def with_translation(translation_options, to_top=False):
    def wrapper(cls):
        if cls.fields:
            if not to_top:
                cls.fields = cls.fields + translation_options.fields
            else:
                cls.fields = translation_options.fields + cls.fields
        else:
            cls.fields = translation_options.fields
        return cls
    return wrapper


class TitledTranslationOptions(TranslationOptions):
    fields = ('title',)

with_title_translation = with_translation(TitledTranslationOptions)


class MetaFieldedTranslationOptions(TranslationOptions):
    fields = ('meta_title', 'meta_description', 'meta_keywords',)

with_metafields_translation = with_translation(MetaFieldedTranslationOptions)
