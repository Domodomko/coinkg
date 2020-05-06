from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kg', 'en')


@register(SuccessStory)
class SuccessStoryTranslationOption(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru', 'kg', 'en')


@register(AboutUs)
class AboutUsTranslationOption(TranslationOptions):
    fields = ('content',)
    required_languages = ('ru', 'kg', 'en')


@register(CreditsInfo)
class CreditsInfoTranslationOption(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = ('ru', 'kg', 'en')


