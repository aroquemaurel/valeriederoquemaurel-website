from django.conf.urls import url
from django.views.generic import ListView

from . import views
from . import models

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.category),
    url(r'^(?P<slug_cat>[\w-]+)/(?P<slug_subcat>[\w-]+)/$', views.sub_category),
    url(r'^$', views.category_list),
]

