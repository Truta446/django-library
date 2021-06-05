from django.contrib import admin
from .models import Author

class ShowAuthor(admin.ModelAdmin):
    list_display = ('name', 'age', 'nacionality')
    list_display_links = ('name',)
    search_fields = ('name', 'nacionality')
    list_filter = ('nacionality',)
    list_per_page = 10

admin.site.register(Author, ShowAuthor)
