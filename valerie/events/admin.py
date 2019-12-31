from django.contrib import admin

from valerie.events.models import Event, ImageAttachmentEvent, DocumentAttachmentEvent

admin.site.register(Event)
admin.site.register(ImageAttachmentEvent)
admin.site.register(DocumentAttachmentEvent)
