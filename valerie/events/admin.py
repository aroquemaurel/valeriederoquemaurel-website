from django.contrib import admin

from valerie.common.admin import admin_method_attributes
from valerie.events.models import Event, ImageAttachmentEvent, DocumentAttachmentEvent


class EventsAttachmentInline(admin.TabularInline):
    raw_id_fields = ('event',)
    min_num = 0
    extra = 0


class EventsImagesInline(EventsAttachmentInline):
    model = ImageAttachmentEvent


class EventsDocInline(EventsAttachmentInline):
    model = DocumentAttachmentEvent


class EventsAdmin(admin.ModelAdmin):
    list_display = ('label_event', 'title', 'start_date', 'end_date', 'location')
    list_display_links = ('label_event', 'title', 'start_date', 'end_date', 'location')
    list_filter = ('start_date', 'end_date', 'location')
    date_hierarchy = 'start_date'
    ordering = '-start_date', '-end_date'
    search_fields = 'title', 'location', 'description', 'start_date', 'end_date'
    fields = 'title', 'start_date', 'end_date', 'location', 'url', 'description'

    inlines = [
        EventsImagesInline,
        EventsDocInline,
    ]

    @staticmethod
    @admin_method_attributes(short_description='Label', allow_tags=True)
    def label_event(event):
        return event.get_label()


admin.site.register(Event, EventsAdmin)
