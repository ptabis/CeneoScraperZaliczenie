from templates import app
from flask import render_template, redirect
from Opinions import Opinions

@app.route('/extract')
def extract():
    return render_template("extract.html", subname="Ekstrakcja opinii")

@app.route('/extract/<id>')
def extract_product(id):
    try:
        opinions = Opinions.get_opinions(int(id))
        opinions.insert_to_database()
    except:
        return render_template("extract.html", subname="Ekstrakcja opinii", mod="extract", error=1)
    return redirect('/product/'+str(id))