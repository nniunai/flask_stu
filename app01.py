from flask import Flask,render_template



app01 =Flask(__name__)


@app01.route("/about")
def about():
    return render_template("about.html")