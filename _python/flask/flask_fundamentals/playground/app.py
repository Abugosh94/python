from flask import Flask, render_template
app = Flask(__name__) 

#Have the /play route render a template with 3 blue boxes
@app.route("/play")
def default_play():
    return render_template("play.html", boxes = 3)

#Have the /play/<x> route render a template with x number of blue boxes
@app.route("/play/<int:number>")
def user_play(number):
    return render_template("play.html", boxes = number)

#Have the /play/<x>/<color> route render a template with x number of boxes the color of the provided value
@app.route("/play/<int:number>/<color>")
def user_play_color(number, color):
    return render_template("play.html", boxes = number, colormsg= color)

if __name__=="__main__": 
    app.run(debug=True) 