from django.urls import path

from .views import note_search

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_note, name="add_note"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
    path('note_search/', note_search, name='note_search'),
    path("account/registration/", views.registration, name="registration")
]
