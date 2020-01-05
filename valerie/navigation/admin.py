# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from valerie.navigation.models import Category
from valerie.pages.models import Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'default_page')
    list_filter = ('title', 'parent')
    ordering = 'title',
    search_fields = 'title', 'parent', 'default_page'
    fields = 'title', 'slug', 'parent', 'default_page', 'img_mini'


admin.site.register(Category, CategoryAdmin)
