# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from valerie.common.admin import admin_method_attributes
from valerie.navigation.models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'get_default_page')
    list_filter = ('parent', )
    ordering = 'title',
    search_fields = 'title', 'parent', 'default_page'
    fields = 'title', 'slug', 'parent', 'default_page', 'img_mini'

    @staticmethod
    @admin_method_attributes(short_description='Page par défaut', allow_tags=True)
    def get_default_page(photo):
        return photo.get_default_page()


admin.site.register(Category, CategoryAdmin)
