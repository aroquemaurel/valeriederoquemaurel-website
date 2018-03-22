from django.conf.urls import url

import valerie
from . import views

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', valerie.navigation.views.display_category, name='display_category'),
    url(r'^(?P<slug_cat>[\w-]+)/(?P<slug_subcat>[\w-]+)/$', valerie.navigation.views.display_subcategory, name='display_subcategory'),
    url(r'^(?P<slug_cat>[\w-]+)/(?P<slug_subcat>[\w-]+)/?P<id_page>[\d]+-[\w-]+$', valerie.navigation.views.display_page, name='display_page'),
]

