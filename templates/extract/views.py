from templates import app
from flask import render_template

@app.route('/extract')
def extract():
    return render_template("extract.html", subname="Ekstrakcja opinii")