from django.shortcuts import render, redirect
import random

#In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
def index(request):
    if "guess" not in request.session:
        request.session["attempt"] = 0 
        request.session["guess"] = 0
    if "number" not in request.session:
        request.session["number"] = random.randint(1,100)
    print(request.session["number"])
    return render(request, "index.html")

#Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
def guess(request):
    request.session["guess"] = int(request.POST["guess"])
    request.session["attempt"] += 1
    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")