from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', views.category),
    url(r'^(?P<slug_cat>[\w-]+)/(?P<slug_subcat>[\w-]+)/$', views.sub_category),
]

