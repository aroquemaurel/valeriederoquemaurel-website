from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^([\w-]+)/([\w-]+)/(?P<id_photo>\d+)-([\w-]+)$', views.display_photo),
]

