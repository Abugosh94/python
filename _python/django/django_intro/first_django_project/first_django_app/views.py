from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

#/blogs - display the string "placeholder to later display a list of all blogs" with a method named "index"
def index(request):
    return HttpResponse("Placeholder to later display a list of all blogs")

#/ - redirects to the "/blogs" route with a method called "root"
def root(request):
    return redirect("/blogs")

#/blogs/new - display the string "placeholder to display a new form to create a new blog" with a method named "new"
def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

#/blogs/create - redirect to the "/" route with a method called "create"
def create(request):
    return redirect("/")

#/blogs/< number > - display the string "placeholder to display blog number: {number}" with a method named "show" 
def show(request, number):
    return HttpResponse(f"Placeholder to display blog number: {number}")

#/blogs/< number >/edit - display the string "placeholder to edit blog {number}" with a method named "edit"
def edit(request, number):
    return HttpResponse(f"Placeholder to edit blog {number}")

#/blogs/< number >/delete - redirect to the "/blogs" route with a method called "destroy"
def destroy(request,number):
    return redirect("/")

#(**Bonus**) /blogs/json - return a JsonResponse with title and content keys.
def json(request):
    return JsonResponse({"title":"Example", "Content":"TBD"})
