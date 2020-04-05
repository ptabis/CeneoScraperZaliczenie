from templates import app
from flask import render_template

@app.route('/about/')
def about():
    return render_template("about.html", subname="O autorze", mod="about")