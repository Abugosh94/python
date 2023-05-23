import random
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "Secret Key"

@app.route("/")
def default_page():
    if "gold" not in session:
        session["gold"]= 0
        session["activity"] = []
        session["moves"] = 0
        session["status"] = "none"
    
    if(session["moves"] == 15 and session["gold"] < 500 ):
        session["status"] = "lose"
    elif(session["moves"] < 15 and session["gold"] >= 500):
        session["status"] = "win"

    status = session["status"]
    gold = session["gold"]
    activities = session["activity"]
    moves = session["moves"]

    return render_template("index.html", gold = gold, activities = activities, moves = moves, status= status)

#Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route
#SENSEI BONUS: Have the activities display in descending order, with the most recent activity first (Which is done by using insert)
@app.route("/process_money", methods=["POST"])
def guess():
    session["moves"] +=1
    if request.form["which_form"] == "farm":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(10,20)
        session["gold"] += result
        session["activity"].insert(0, f"Earned {result} gold from the farm! ({timestamp})")

    elif request.form["which_form"] == "cave":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(5,10)
        session["gold"] += result
        session["activity"].insert(0, f"Earned {result} gold from the cave! ({timestamp})")

    elif request.form["which_form"] == "house":
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        result = random.randint(2,5)
        session["house"] += result
        session["activity"].insert(0, f"Earned {result} gold from the house! ({timestamp})")

    elif request.form["which_form"] == "casino":
        rng = random.randint(1,100)
        result = random.randint(0,50)
        now = datetime.now()
        timestamp = now.strftime("%Y/%m/%d %I:%M:%S %p")
        if result == 0:
            session["activity"].insert(0, f"Entered a casino and didn't lose or make profit. ({timestamp})")
        elif rng%3 == 0:
            session["gold"] += result
            session["activity"].insert(0, f"Entered a casino and earned {result} gold! ({timestamp})")
        else:
            session["gold"] -= result
            session["activity"].insert(0, f"Entered a casino and lost {result} gold.. Ouch.. ({timestamp})")

    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__": 
    app.run(debug=True) 