from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest
from django.http.response import HttpResponse

from .models import Book

def index(request: HttpRequest) -> HttpResponse:
    data = {
        'books': Book.objects.all()
    }

    return render(request, 'index.html', data)

def book(request: HttpRequest, book_id: int) -> HttpResponse:
    book = {
        'book': get_object_or_404(Book, pk=book_id)
    }

    return render(request, 'book.html', book)

def loan(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('index')

    data = {
        'books': Book.objects.filter(borrowed=False)
    }

    return render(request, 'index.html', data)

def search(request: HttpRequest) -> HttpResponse:
    books = Book.objects.order_by('title').all()

    if 'title' in request.GET:
        title = request.GET['title']

        if title:
            books = books.filter(title__icontains=title)

    data = {
        'books': books
    }

    return render(request, 'index.html', data)