from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(News)
class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'content')
    required_languages = ('ru',)


@register(SuccessStory)
class SuccessStoryTranslationOption(TranslationOptions):
    fields = ('title', 'content')


@register(AboutUs)
class AboutUsTranslationOption(TranslationOptions):
    fields = ('content',)


@register(CreditsInfo)
class CreditsInfoTranslationOption(TranslationOptions):
    fields = ('title', 'content',)


