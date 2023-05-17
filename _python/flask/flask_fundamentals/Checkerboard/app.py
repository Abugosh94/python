from flask import Flask, render_template
app = Flask(__name__) 

#Have the root route render a template with a checkerboard on it
@app.route("/")
def default():
    return render_template("checkerboard.html", x = 8 , y=8)

#Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route("/<int:number>")
def user_play(number):
    return render_template("checkerboard.html", x = number , y=8)

#NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route("/<int:number>/<int:number2>")
def user_play2(number, number2):
    return render_template("checkerboard.html", x = number , y=number2)

#SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") 
#and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route("/<int:number>/<int:number2>/<color1>/<color2>")
def user_play_color(number, number2, color1, color2):
    return render_template("checkerboard.html", x = number , y=number2, colormsg1= color1, colormsg2= color2)

if __name__=="__main__": 
    app.run(debug=True) 