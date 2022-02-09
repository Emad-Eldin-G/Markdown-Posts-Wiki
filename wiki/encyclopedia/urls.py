from unicodedata import name
from django.urls import path

from . import views
from . import util 

app_name = "encyclopedia"

urlpatterns = [

    path("", views.index, name="index"),
    path("wiki/<entry>", views.entry, name="EntryPage"),
    path("new", views.new_page, name="NewPage"),
    path("random/", views.random_entry, name="RandomEntry"),
    path("wiki/<entry>/edit/", views.edit, name="edit"),
    path("Search", views.search, name="Search")
]
