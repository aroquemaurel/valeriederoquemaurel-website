from django.conf.urls import url

import valerie
from . import views

urlpatterns = [
    url(r'^$', valerie.pages.views.index),
]

