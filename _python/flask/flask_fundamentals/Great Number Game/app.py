import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "Secret Key"

#In the root route, save a random number between 1 and 100 and display a form for the user to guess the number
@app.route("/")
def default_page():
    if "guess" not in session:
        session["attempt"] = 0 
        session["guess"] = 0
    if "number" not in session:
        session["number"] = random.randint(1,100)
    return render_template("index.html", number = session["number"], guess= session["guess"], tries = session["attempt"])

#Create a route that determines whether the number submitted is too high, too low, or correct. Show this status on the HTML page.
@app.route("/guess", methods=["POST"])
def guess():
    session["guess"] = int(request.form["guess"])
    session["attempt"] += 1
    return redirect("/")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__=="__main__": 
    app.run(debug=True) 