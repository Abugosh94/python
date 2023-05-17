from flask import Flask, render_template
app = Flask(__name__) 

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


#Create a route in which the data above is declared and then sent to the template engine to be rendered
@app.route("/")
def default():
    return render_template("html_table.html", users=users)

if __name__=="__main__": 
    app.run(debug=True) 