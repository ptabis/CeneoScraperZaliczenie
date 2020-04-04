from templates import app
from flask import render_template, redirect, url_for
from Database import DB

@app.route('/product/<id>')
def product(id):
    cursor = DB.cursor(dictionary=True)
    cursor.execute("SELECT * FROM opinions WHERE id=%s", (id,))
    res = cursor.fetchall()
    print(res)
    return render_template("product.html", subname=f"Produkt - {id}", id=id, mod="product", res=res)
