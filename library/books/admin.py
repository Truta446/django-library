from django.contrib import admin
from .models import Book

class ShowBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'editor', 'publication_year', 'isbn', 'borrowed')
    list_display_links = ('title',)
    search_fields = ('title', 'author', 'editor')
    list_filter = ('author', 'editor')
    list_editable = ('borrowed',)
    list_per_page = 10

admin.site.register(Book, ShowBook)
