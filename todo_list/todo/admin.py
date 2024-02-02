from django.contrib import admin

from .models import Note, Category

# Register your models here.

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass