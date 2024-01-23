from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .models import Note
from .forms import NoteForm

def index(request):
    notes = Note.objects.filter(user_id=request.user.id)
    return render(request, "index.html", {"notes": notes})

@login_required()
def add_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Věc byla přidána.")
            return redirect("index")
    else:
        form = NoteForm()
    return render(request, "add_note.html", {"form":form})


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()
    return render(request, "registration/registration.html", {"form": form})


