from templates import app
from flask import render_template, redirect, url_for
from Database import DB

@app.route('/product/<id>')
def product(id):
    cursor = DB.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
    product = cursor.fetchall()

    cursor.execute("SELECT * FROM opinions WHERE product_id=%s", (id,))
    opinions = cursor.fetchall()

    return render_template("product.html", subname=f"Produkt - {id} - {product[0]['name']}", id=id, mod="product", opinions=opinions, product=product[0])
