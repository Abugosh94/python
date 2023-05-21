from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = "Secret Key"

#Have the root route render a template that displays the number of times the client has visited this site. Refresh the page several times to ensure the counter is working.
@app.route("/")
def default_page():
    #SENSEI BONUS: Adjust your code to display both how many times the user has actually visited the page, 
    #as well as the value of the counter, given the above functionality
    if "visits" not in session:
        session["visits"]=0
    if "count" in session:
        print('count exists!')
        session["count"]+=1
    else:
        print("key 'count' does NOT exist")
        session["count"]=1

    session["visits"] +=1 
    return render_template("index.html", count = session["count"], visits = session["visits"] )

#NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route("/addtwo")
def addtwo():
    session["count"]+=1

    return redirect("/")

#SENSEI BONUS: Add a form that allows the user to specify the increment of the counter and have the counter increment accordingly
@app.route("/addcustom", methods=["POST"])
def addcustom():
    amount = int(request.form["amount"]) -1 
    session["count"]+=amount
    return redirect("/")

#NINJA BONUS: Add a Reset button to reset the counter
@app.route("/destroy")
def destroy():
    session.pop("count")
    return redirect("/")

#Add a "/destroy_session" route that clears the session and redirects to the root route. Test it.
@app.route("/destroy_session")
def destroysession():
    session.clear()
    return redirect("/")

if __name__=="__main__": 
    app.run(debug=True) 