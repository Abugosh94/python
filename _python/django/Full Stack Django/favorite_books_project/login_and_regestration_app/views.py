from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from login_and_regestration_app.models import *

def index(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            return redirect("/success")
    return render(request, 'index.html')


def success(request):
    if request.session["status"] == "Logged In":
        context = {
            "user": User.objects.get(id=request.session['userid'])
        }
        return redirect('/books')
    if request.session["status"] == "Registered":
        return render (request, 'success.html')
    return redirect("/")
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        password = request.POST["pass"]
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        new_user = User(fname= request.POST["fname"], lname= request.POST["lname"], email= request.POST["email"], password = pw_hash)
        new_user.save()
        request.session["status"]="Registered"
        return redirect('/success')
    
def login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        this_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode() , this_user.password.encode()):
            request.session['userid'] = this_user.id
            request.session["status"] = "Logged In"
            return redirect('/success')
    
    request.session['incorrect'] = 'Please check your Email and Password'
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect("/")