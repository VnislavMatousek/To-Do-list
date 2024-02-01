from django.forms import ModelForm
from django import forms

from .models import Note, Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ["user"]


class NoteForm(ModelForm):
    class Meta:
        model = Note
        exclude = ["user"]

class NoteSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='Search by Title')