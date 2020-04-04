from templates import app
from flask import render_template, redirect
from Product import Product

@app.route('/extract')
def extract():
    return render_template("extract.html", subname="Ekstrakcja opinii", mod="extract")

@app.route('/extract/<id>')
def extract_product(id):
    try:
        product = Product.get_product(int(id))
        product.insert_to_database()
    except:
        return render_template("extract.html", subname="Ekstrakcja opinii", mod="extract", error=1)
    return redirect('/product/'+str(id))