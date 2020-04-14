from django.urls import path

from . import views

app_name = "graph_notes"
urlpatterns = [
    # /graph_notes
    path("", views.index, name="index"),
    # /graph_notes/4
    path("<int:note_id>/", views.detail, name="detail"),
    # /graph_notes/create
    path("create/", views.create, name="create"),
    # /graph_notes/save_note
    path("save_note/", views.save, name="save_note"),
]
