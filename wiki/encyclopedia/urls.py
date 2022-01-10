from django.urls import path

from . import views, util

app_name = "encyclopedia"

urlpatterns = [

    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry_page, name="EntryPage"),
    path("new", views.new_page, name="NewPage")
]
