from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from login_and_regestration_app.models import *
from kickball_league_app.models import *

def index(request):
    if "status" in request.session:
        if request.session["status"] == "Logged In":
            return redirect("/home")
    return render(request, 'index.html')

def home(request):
    if "status" in request.session and request.session["status"] == "Logged In":
        teams = Team.objects.all().order_by('-created_at')
        context={
            "logged_user": User.objects.get(id= request.session['userid']),
            "teams": teams
        }
        return render(request, 'home.html', context)
    return redirect("/")


def success(request):
    return redirect('/home')

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
        messages.error(request,"Register Succesfull!")
        return redirect('/')
    
def login(request):
    user = User.objects.filter(email=request.POST['login_email'])
    if user:
        this_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode() , this_user.password.encode()):
            request.session['userid'] = this_user.id
            request.session["status"] = "Logged In"
            return redirect('/home')
    
    messages.error(request,"Please check your Email and Password") 
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect("/")