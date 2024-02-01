from django.urls import path

from .views import note_search

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_note, name="add_note"),
    path("category/", views.add_category, name="add_category"),
    path("categories/", views.categories, name="note_categories"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("editcategory/<int:category_id>/", views.edit_category, name="edit_category"),
    path("delete/<int:note_id>/", views.delete_note, name="delete_note"),
    path("deletecategory/<int:category_id>/", views.delete_category, name="delete_category"),
    path('note_search/', note_search, name='note_search'),
    path("account/registration/", views.registration, name="registration")
]
