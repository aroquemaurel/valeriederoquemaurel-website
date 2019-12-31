from django.contrib import admin

from valerie.events.models import Event, ImageAttachmentEvent, DocumentAttachmentEvent


def label_event(event):
    return event.get_label()


class EventsAdmin(admin.ModelAdmin):
    list_display = (label_event, 'title', 'start_date', 'end_date', 'location')
    list_display_links = (label_event, 'title', 'start_date', 'end_date', 'location')
    list_filter = ('start_date', 'end_date', 'location')
    date_hierarchy = 'start_date'
    ordering = '-start_date', '-end_date'
    search_fields = 'title', 'location', 'description', 'start_date', 'end_date'


admin.site.register(Event, EventsAdmin)
admin.site.register(ImageAttachmentEvent)
admin.site.register(DocumentAttachmentEvent)
