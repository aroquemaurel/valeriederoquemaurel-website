# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def display_photo(request, id_photo):
    # TODO AR : afficher categorie, sous categorie, liste sous categorie et photo associé en paramètre
    return HttpResponse("Photo : "+id_photo)


