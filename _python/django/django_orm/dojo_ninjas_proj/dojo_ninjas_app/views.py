from django.shortcuts import render, redirect
from dojo_ninjas_app.models import *

def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }

    return render(request, "index.html", context)

def process(request):
    if(request.POST["form_name"] == "dojo_form"):
        new_dojo = Dojo(name= request.POST["name"], city= request.POST["city"], state= request.POST["state"])
        new_dojo.save()

    else:
        new_ninja = Ninja(first_name= request.POST["fname"], last_name= request.POST["lname"], dojo= Dojo.objects.get(name = request.POST["dojo"]))
        new_ninja.save()

    return redirect('/')