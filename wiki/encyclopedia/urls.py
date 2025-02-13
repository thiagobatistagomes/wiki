from django.urls import path

from . import views

app_name = "entries"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.getEntry, name="entry"),
    path("search/", views.searchEntries, name="search"),
    path("new/", views.createEntry, name="create"),
    path("edit/<str:entry>/", views.editEntry, name="edit"),
    path("random/", views.randomEntry, name="random")
]
