from django.shortcuts import render, redirect
from dojo_reads_app.models import *
from login_and_regestration_app.models import *

def books(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            this_user = User.objects.get(id=request.session["userid"])
            books = Book.objects.all().order_by('-created_at')[:5]
            other_books = Book.objects.all()
            for book in books:
                other_books = other_books.exclude(title=book.title)
            context = {
                "logged_user": this_user,
                "books": books,
                "other_books": other_books,
            }
            return render(request, 'books.html', context)
    return redirect("/")

def add_book(request):
    context = {
        "authors": Author.objects.all(),
    }
    return render(request, "add_book.html", context)

def process(request):
    this_user = User.objects.get(id=request.session["userid"])
    new_review = Review(description = request.POST["review"], rating= int(request.POST["rating"]), user = this_user)
    new_review.save()
    if request.POST["new_author"]:
        new_author = Author(first_name= request.POST["new_author"], last_name= request.POST["new_author"])
        new_author.save()
        new_book = Book(title= request.POST["title"], review= new_review, author = new_author)
        new_book.save()
        return redirect('/books')
    else:
        new_book = Book(title= request.POST["title"], review= new_review, author = Author.objects.get(id=int(request.POST["author"])))
        new_book.save()


    return redirect('/books')