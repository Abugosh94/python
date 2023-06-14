from django.shortcuts import render, redirect
from semi_restful_tv_shows_app.models import *
from datetime import date

def index(request):
    context={
        "movies": Movie.objects.all()
    }
    return render(request, "index.html", context)

def to_index(request):
    return redirect('/shows')

def new(request):
    return render (request, "new.html")

def create(request):
    new_movie = Movie(title= request.POST["title"], desc= request.POST["desc"], network= request.POST["network"], release_date= request.POST["release_date"])
    new_movie.save()


    return redirect('/shows')


def view(request, id):
    context = {
        "movie": Movie.objects.get(id=id)
    }

    return render(request, 'view.html', context)

def edit(request, id):
    context = {
        "movie": Movie.objects.get(id=id),
        "date": Movie.objects.get(id=id).release_date.strftime("%Y-%m-%d")
    }

    return render(request, 'update.html', context)

def update(request, id):
    movie = Movie.objects.get(id=id)
    movie.title= request.POST["title"] 
    movie.desc= request.POST["desc"]
    movie.network= request.POST["network"]
    movie.release_date= request.POST["release_date"]
    movie.save()
    
    return redirect(f'/shows/{id}')

def destroy(request, id):
    Movie.objects.get(id=id).delete()

    return redirect('/shows')
