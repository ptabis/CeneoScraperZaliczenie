from templates import app
from flask import render_template

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html", subname="Strona główna", mod="home")
