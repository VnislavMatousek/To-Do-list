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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['categories'].queryset = Category.objects.filter(user_id=user.id)


class NoteSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False, label='Search by Title or Category')
