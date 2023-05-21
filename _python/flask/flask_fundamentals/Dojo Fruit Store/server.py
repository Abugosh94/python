from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    #When the Checkout button is clicked, have the correct information display on the checkout.html page
    firstname = request.form["first_name"]
    lastname = request.form["last_name"]
    id = request.form["student_id"]
    strawberries = int(request.form["strawberry"])
    raspberries = int(request.form["raspberry"])
    apples = int(request.form["apple"])
    now = datetime.now()
    count = strawberries+raspberries+apples
    datenow = now.strftime("%B %d, %Y %H:%M:%S")
    #In the checkout method, add a print statement that says "Charging {{Customer name}} for {{count}} fruits"
    #It will keep charging student (calling the method) when page is refreshed
    print(f"Charging {firstname} for {count} fruits")
    return render_template("checkout.html", 
                        firstname = firstname,
                        lastname = lastname,
                        id = id,
                        strawberries = strawberries,
                        raspberries = raspberries,
                        apples = apples,
                        count = count,
                        datenow = datenow
                        )
@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    