from django.shortcuts import render, redirect
from django.contrib import messages
from courses_app.models import *

def index(request):
    context={
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)


def create(request):
    errors = Course.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        new_course = Course(name= request.POST["name"])
        new_course.save()
        new_desc = Description.objects.create(content= request.POST["desc"], course= new_course)
        new_desc.save()
        return redirect('/')

def confirm(request, id):
    context={
        "course": Course.objects.get(id=id)
    }
    return render(request, "delete.html", context)

def delete(request, id):
    Course.objects.get(id=id).delete()

    return redirect('/')

def course(request, id):
    context={
        "course": Course.objects.get(id=id),
        "comments": Comment.objects.filter(course= Course.objects.get(id=id))
    }
    print(Course.objects.get(id=id))
    return render(request, "view.html", context)

def add_comment(request, id):
    this_course = Course.objects.get(id=id)
    new_comment = Comment.objects.create(content= request.POST["content"], course= this_course)
    new_comment.save()

    return redirect(f'/courses/{id}')