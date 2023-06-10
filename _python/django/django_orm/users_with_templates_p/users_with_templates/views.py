from django.shortcuts import render, redirect
from users_with_templates.models import *

def index(request):
    context = {
        "all_users": Users.objects.all()
    }
    return render(request, "index.html", context)

def process(request):
    new_user = Users(first_name= request.POST["fname"], last_name= request.POST["lname"], email_address= request.POST["email"], age= request.POST["age"])
    new_user.save()
    return redirect('/')