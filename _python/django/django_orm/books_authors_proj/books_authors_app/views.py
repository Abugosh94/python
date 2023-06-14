from django.shortcuts import render, redirect
from books_authors_app.models import *

def index(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }

    return render(request, "index.html", context)

def books(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }

    return render(request, "add_book.html", context)

def authors(request):
    context = {
        "books": Book.objects.all(),
        "authors": Author.objects.all()
    }

    return render(request, "add_author.html", context)

def display(request,title):
    book = Book.objects.get(title=title.capitalize())
    authors = book.authors.all()
    context = {
        "book": book,
        "authors": authors
    }
    return render(request, "display_book.html", context)

def display_author(request,id):
    author = Author.objects.get(id=id)
    book = author.books.all()
    context = {
        "author": author,
        "books": book
    }
    return render(request, "display_author.html", context)

def process(request):
    if(request.POST["form_name"] == "book_form"):
        new_book = Book(title= request.POST["title"], desc= request.POST["desc"])
        new_book.save()
        author = Author.objects.get(id=(int(request.POST["author_name"])))
        new_book.authors.add(author)


    else:
        new_author = Author(first_name= request.POST["fname"], last_name= request.POST["lname"])
        new_author.save()
        book = Book.objects.get(id=(int(request.POST["book_name"])))
        new_author.books.add(book)


    return redirect('/')