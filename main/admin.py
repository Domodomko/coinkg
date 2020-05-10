from django.contrib import admin
from django.contrib.admin import ModelAdmin

from modeltranslation.admin import TranslationAdmin

from main.models import *


class NewsAdmin(TranslationAdmin, ModelAdmin):
    list_display = ('title', 'publish', 'views')
    search_fields = ('title',)
    readonly_fields = ('views', 'publish')
    ordering = ('publish',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = [
        (u'News', {'fields': ('title', 'content', 'image', 'views',)})
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class SuccessStoryAdmin(TranslationAdmin):
    fieldsets = [
        (u'SuccessStory', {'fields': ('title', 'content')})
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class AboutUsAdmin(TranslationAdmin):
    fieldsets = [
        (u'AboutUs', {'fields': ('content',)})
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'content', 'publish',)
    search_fields = ('name', 'publish')
    readonly_fields = ('name', 'email', 'phone', 'content', 'publish')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = [
        (u'Feedback', {'fields': ('name', 'email', 'phone', 'content', 'publish')})
    ]


class CreditAdmin(admin.ModelAdmin):
    list_display = ('product', 'sum', 'time', 'passport', 'user', 'verify')
    search_fields = ('product', 'sum', )
    readonly_fields = ('publish',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CreditsInfoAdmin(TranslationAdmin):
    fieldsets = [
        (u'Credit', {'fields': ('title', 'content', 'image')})
    ]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(News, NewsAdmin)
admin.site.register(SuccessStory, SuccessStoryAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Contact)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Credit, CreditAdmin)
admin.site.register(CreditsInfo, CreditsInfoAdmin)
