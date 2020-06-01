# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from valerie.common.admin import admin_method_attributes
from valerie.common.string_helper import preview_content
from valerie.press.models import Article, ImageAttachmentArticle


class ArticleImagesInline(admin.TabularInline):
    raw_id_fields = ('article', )
    min_num = 1
    extra = 1
    model = ImageAttachmentArticle


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date', )
    date_hierarchy = 'date'
    ordering = ('-date', )
    search_fields = 'title', 'date'
    fields = 'title', 'date'

    inlines = [
        ArticleImagesInline
    ]

    @staticmethod
    @admin_method_attributes(short_description='Contenu', allow_tags=True)
    def preview_content(article):
        return preview_content(article.content)


admin.site.register(Article, ArticleAdmin)
