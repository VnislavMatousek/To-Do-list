from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Q

from .forms import NoteSearchForm

from .models import Note, Category
from .forms import NoteForm, CategoryForm


def index(request):
    notes = Note.objects.filter(user_id=request.user.id)
    return render(request, "index.html", {"notes": notes})

@login_required()
def categories(request):
    categories = Category.objects.filter(user_id=request.user.id)
    return render(request, "categories.html", {"categories": categories})

@login_required()
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST, user=request.user)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save_m2m()
            messages.add_message(request, messages.INFO, "Note was added.")
            return redirect("index")
    else:
        form = NoteForm(user=request.user)
    return render(request, "add_note.html", {"form":form})

@login_required()
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Category was added.")
            return redirect("note_categories")
    else:
        form = CategoryForm()
    return render(request, "add_category.html", {"form":form})

@login_required()
def note_search(request):
    form = NoteSearchForm(request.GET)
    notes = Note.objects.filter(user_id=request.user.id)

    if form.is_valid():
        title_query = form.cleaned_data.get('title')
        if title_query:
            notes = notes.filter(Q(title__icontains=title_query) | Q(categories__name=title_query))

    context = {'form': form, 'notes': notes}
    return render(request, 'note_search.html', context)

@login_required()
def edit_note(request, note_id):
    note = get_object_or_404(Note,id=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note, user=request.user)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Note was edited.")
            return redirect("index")  # Upravte název cesty podle vašich potřeb
    else:
        form = NoteForm(instance=note, user=request.user)

    return render(request, "edit_note.html", {"form": form, "note": note})

@login_required()
def edit_category(request, category_id):
    category= get_object_or_404(Category,id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Category was edited.")
            return redirect("note_categories")  # Upravte název cesty podle vašich potřeb
    else:
        form = CategoryForm(instance=category)

    return render(request, "edit_category.html", {"form": form, "category": category})

@login_required()
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    note.delete()
    messages.add_message(request, messages.INFO, "Note was deleted.")
    return redirect("index")  # Upravte název cesty podle vašich potřeb

@login_required()
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id, user=request.user)

    category.delete()
    messages.add_message(request, messages.INFO, "Category was deleted.")
    return redirect("note_categories")  # Upravte název cesty podle vašich potřeb

    

def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Registration was successful.")
            return redirect("login")

    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})


