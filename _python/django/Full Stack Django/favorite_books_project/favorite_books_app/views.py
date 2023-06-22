from django.shortcuts import render, redirect
from favorite_books_app.models import *
from login_and_regestration_app.models import *

def books(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            this_user = User.objects.get(id=request.session["userid"])
            context = {
                "logged_user": this_user,
                "books": Book.objects.all,
                "favorites": this_user.books.all(),
            }
            return render(request, 'books.html', context)
    return redirect("/")

def create(request):
    new_book = Book(title= request.POST["title"], desc = request.POST["desc"], uploaded_by= User.objects.get(id=request.session["userid"]))
    new_book.save()
    return redirect('/books')

def add_favorite(request, id):
    new_fav = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session["userid"])
    new_fav.favorites.add(this_user)
    return redirect('/books')

def remove_favorite(request, id):
    book = Book.objects.get(id=id)
    this_user = User.objects.get(id=request.session["userid"])
    book.favorites.remove(this_user)
    return redirect(f'/books/{id}')

def view(request, id):
    this_book = Book.objects.get(id=id)
    logged_user = User.objects.get(id=request.session["userid"])

    if logged_user.books.filter(id=id):
        logged_user_is_fav = True
    else:
        logged_user_is_fav = False

    context = {
        "logged_user": logged_user,
        "book": this_book,
        "users": this_book.favorites.all(),
        "logged_user_is_fav": logged_user_is_fav,
    }
    return render(request, 'view.html', context)

def view_favs(request):
    logged_user = User.objects.get(id=request.session["userid"])
    logged_user_favs = logged_user.books.all()

    context = {
        "logged_user": logged_user,
        "logged_user": logged_user,
        "logged_user_favs": logged_user_favs,
    }
    return render(request, 'favs.html', context)

def delete(request, id):
    this_book = Book.objects.get(id=id)
    if request.session["userid"] == this_book.uploaded_by.id:
        this_book.delete()

    return redirect('/books')