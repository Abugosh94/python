from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "Secret Key"

#Have the root route ("/") show a page with the form
@app.route("/")
def default_page():
    if "visits" not in session:
        session["visits"]=1
    if "count" in session:
        print('count exists!')
        session["count"]+=1
    else:
        print("key 'count' does NOT exist")
        session["count"]=1

    session["visits"] +=1 
    return render_template("index.html", count = session["count"], visits = session["visits"] )

@app.route("/addtwo")
def addtwo():
    session["count"]+=1

    return redirect("/")

@app.route("/addcustom", methods=["POST"])
def addcustom():
    amount = int(request.form["amount"]) -1 
    session["count"]+=amount
    return redirect("/")

#Have the "/result" route display the information from the form on a new HTML page
@app.route("/destroy")
def destroy():
    session.pop("count")
    return redirect("/")

if __name__=="__main__": 
    app.run(debug=True) 