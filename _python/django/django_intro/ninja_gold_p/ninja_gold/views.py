from django.shortcuts import render, redirect
from datetime import datetime
import random

def index(request):
    if "gold" not in request.session:
        request.session["gold"]= 0
        request.session["activity"] = []
        request.session["moves"] = 0
        request.session["status"] = "none"
        request.session["moves_condition"] = 15
        request.session["gold_condition"] = 500
    
    if(request.session["moves"] == request.session["moves_condition"] and request.session["gold"] < request.session["gold_condition"] ):
        request.session["status"] = "lose"
    elif(request.session["moves"] <= request.session["moves_condition"] and request.session["gold"] >= request.session["gold_condition"]):
        request.session["status"] = "win"

    return render(request, "index.html")

def rules(request):
    request.session["moves_condition"] = int(request.POST["moves"])
    request.session["gold_condition"] = int(request.POST["gold"])

    return redirect("/")

#Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
#SENSEI BONUS: Have the activities display in descending order, with the most recent activity first (Which is done by using insert)
def process_money(request):
    request.session["moves"] +=1
    if request.POST["which_form"] == "farm":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(10,20)
        request.session["gold"] += result
        request.session["activity"].insert(0, f"Earned {result} gold from the farm! ({timestamp})")

    elif request.POST["which_form"] == "cave":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(5,10)
        request.session["gold"] += result
        request.session["activity"].insert(0, f"Earned {result} gold from the cave! ({timestamp})")

    elif request.POST["which_form"] == "house":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(2,5)
        request.session["house"] += result
        request.session["activity"].insert(0, f"Earned {result} gold from the house! ({timestamp})")

    elif request.POST["which_form"] == "casino":
        rng = random.randint(1,100)
        result = random.randint(0,50)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if result == 0:
            request.session["activity"].insert(0, f"Entered a casino and didn't lose or make profit. ({timestamp})")
        #because the house always wins
        elif rng%3 == 0:
            request.session["gold"] += result
            request.session["activity"].insert(0, f"Entered a casino and earned {result} gold! ({timestamp})")
        else:
            request.session["gold"] -= result
            request.session["activity"].insert(0, f"Entered a casino and lost {result} gold.. Ouch.. ({timestamp})")

    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
