from django.shortcuts import render
from .models import Book, Genre, Author
# Create your views here.

def index(request):
    # books = Book.objects.filter(status = 'in stock').order_by('title') #query set
    genres = Genre.objects.all()
    return render(request, 'main/index.html', {'genres':genres})

def book_list(request, slug):
    books = Book.objects.filter(genre__slug=slug)
    return render(request, 'main/book_list.html', {'books':books})

def author_detail(request, pk):
    author = Author.objects.get(pk = pk)
    author_books = author.books.all() # accessing all the books of the author with related name 'book'
    return render(request, 'main/author_detail.html', {'author':author, 'author_books': author_books})
