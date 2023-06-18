from django.shortcuts import render, redirect
from django.contrib import messages
from the_wall_app.models import *
from login_and_regestration_app.models import *

def wall(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            context = {
                "user": User.objects.get(id=request.session["userid"]),
                "messages": Message.objects.all(),
                "comments": Comment.objects.all(),
            }
            return render(request, 'wall.html', context)
    return redirect("/")

def create(request):
    new_message = Message(message= request.POST["content"], user= User.objects.get(id=request.session["userid"]))
    new_message.save()
    return redirect('/wall')

def create_comment(request, id):
    new_comment = Comment(comment= request.POST["content"], user= User.objects.get(id=request.session["userid"]), message = Message.objects.get(id=id))
    new_comment.save()
    return redirect('/wall')

def delete(request, id):
    this_message = Message.objects.get(id = id)
    if request.session["userid"] == this_message.user.id:
        this_message.delete()

    return redirect('/wall')