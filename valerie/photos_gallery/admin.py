# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from valerie.common.admin import admin_method_attributes
from valerie.common.string_helper import preview_content
from valerie.navigation.models import Category
from valerie.photos_gallery.models import Photo


class CategoriesListFilter(admin.SimpleListFilter):
    title = _('Catégories')
    parameter_name = 'parent'

    def lookups(self, request, model_admin):
        filter_cat = []
        for cat in Category.objects.all():
            if model_admin.model.objects.filter(parent=cat):
                filter_cat.append(cat)

        return [(c.id, c.title) for c in filter_cat]

    def queryset(self, request, queryset):
        if self.value() is None:
            return queryset

        return queryset.filter(parent__id=self.value())


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('parent', 'title', 'preview_content', 'position')
    list_display_links = ('title', )
    list_filter = (CategoriesListFilter,)
    ordering = 'parent', 'position'
    search_fields = 'title', 'content'

    @staticmethod
    @admin_method_attributes(short_description='Contenu', allow_tags=True)
    def preview_content(photo):
        return preview_content(photo.content)

    @staticmethod
    @admin_method_attributes(short_description='Catégories', allow_tags=True)
    def get_categories(photo):
        return []
    #fields = 'title', 'start_date', 'end_date', 'location', 'url', 'description'


admin.site.register(Photo, PhotoAdmin)
