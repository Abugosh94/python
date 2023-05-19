from flask import Flask, render_template, request, redirect
app = Flask(__name__) 

#Have the root route ("/") show a page with the form
@app.route("/")
def default_page():
    return render_template("survey.html")

#Have the "/result" route display the information from the form on a new HTML page
@app.route("/result", methods=['POST'])
def filldata():
    name_from_form = request.form["name"]
    location_from_form = request.form["location"]
    language_from_form = request.form["language"]
    gender_from_form = request.form["gender"]
    comment_from_form = request.form["comment"]
    return render_template("data.html", 
                            name = name_from_form, 
                            location = location_from_form, 
                            language = language_from_form,
                            gender = gender_from_form,
                            comment = comment_from_form
                        )


if __name__=="__main__": 
    app.run(debug=True) 