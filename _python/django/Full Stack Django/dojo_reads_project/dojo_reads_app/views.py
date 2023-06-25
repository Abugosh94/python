from django.shortcuts import render, redirect
from dojo_reads_app.models import *
from login_and_regestration_app.models import *

def books(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            this_user = User.objects.get(id=request.session["userid"])
            books = Book.objects.all().order_by('-created_at')[:5]
            reviews = Review.objects.all().order_by('-created_at')[:5]
            other_books = Book.objects.all()
            for book in books:
                other_books = other_books.exclude(title=book.title)
            context = {
                "logged_user": this_user,
                "books": books,
                "other_books": other_books,
                "reviews": reviews
            }
            return render(request, 'books.html', context)
    return redirect("/")

def add_book(request):
    this_user = User.objects.get(id=request.session["userid"])
    context = {
        "logged_user": this_user,
        "authors": Author.objects.all(),
    }
    return render(request, "add_book.html", context)

def process(request):
    this_user = User.objects.get(id=request.session["userid"])
    if request.POST["new_author"]:
        new_author = Author(first_name= request.POST["new_author"], last_name= request.POST["new_author"])
        new_author.save()
        new_book = Book(title= request.POST["title"], author = new_author)
        new_book.save()
        new_review = Review(description = request.POST["review"], rating= int(request.POST["rating"]), user = this_user, book = new_book)
        new_review.save()
        return redirect('/books')
    else:
        new_book = Book(title= request.POST["title"], author = Author.objects.get(id=int(request.POST["author"])))
        new_book.save()
        new_review = Review(description = request.POST["review"], rating= int(request.POST["rating"]), user = this_user, book = new_book)
        new_review.save()

    return redirect('/books')

def view_book(request, id):
    this_user = User.objects.get(id=request.session["userid"])
    context = {
        "logged_user": this_user,
        "book": Book.objects.get(id=id),
        "reviews": Book.objects.get(id=id).reviews.all()
    }
    return render(request, "display_book.html", context)

def add_review(request, id):
    this_user = User.objects.get(id=request.session["userid"])
    this_book = Book.objects.get(id=id)

    new_review = Review(description = request.POST["review"], rating= int(request.POST["rating"]), user = this_user, book = this_book)
    new_review.save()
    return redirect(f"/books/{id}")

