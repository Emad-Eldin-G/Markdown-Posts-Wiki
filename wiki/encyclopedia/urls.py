from django.urls import path

from . import views, util



urlpatterns = [

    path("", views.index, name="index"),
    path("<str:entry>", views.entry_page, name="EntryPage"),
    path("/New", views.new_page, name="NewPage")
]
