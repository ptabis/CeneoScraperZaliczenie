from templates import app
from flask import render_template, redirect, url_for, jsonify
from Database import DB

@app.route('/products/')
def products():
    cursor = DB.cursor(dictionary=True)
    cursor.execute("SELECT p.*, COUNT(o.id) AS opinions,\
         COUNT(pr.text) AS pros, COUNT(c.text) AS cons\
         FROM products p\
         LEFT JOIN opinions o ON p.id = o.product_id\
         LEFT JOIN pros pr ON pr.opinion_id = o.id\
         LEFT JOIN cons c ON c.opinion_id = o.id\
         GROUP BY p.id")
    products = cursor.fetchall()
    print(products)

    return render_template("products.html", subname="Lista produktów", mod="products", products=products)

@app.route('/product/<id>/')
def product(id):
    cursor = DB.cursor(dictionary=True)

    cursor.execute("SELECT p.*, COUNT(o.id) AS opinions FROM products p LEFT JOIN opinions o ON p.id = o.product_id WHERE p.id=%s", (id,))
    product = cursor.fetchall()

    cursor.execute("SELECT * FROM opinions WHERE product_id=%s", (id,))
    opinions = cursor.fetchall()

    for opinion in opinions:
        cursor.execute("SELECT text from pros WHERE opinion_id = %s", (opinion['id'],))
        pros = cursor.fetchall()
        opinion['pros'] = pros

    for opinion in opinions:
        cursor.execute("SELECT text from cons WHERE opinion_id = %s", (opinion['id'],))
        cons = cursor.fetchall()
        opinion['cons'] = cons

    return render_template("product.html", subname=f"Produkt - {id} - {product[0]['name']}", id=id, mod="product", opinions=opinions, product=product[0])


@app.route('/product/<id>/json/')
def product_json(id):
    cursor = DB.cursor(dictionary=True)
 
    cursor.execute("SELECT * FROM products p WHERE id=%s", (id,))
    product = cursor.fetchall()

    cursor.execute("SELECT * FROM opinions WHERE product_id=%s", (id,))
    opinions = cursor.fetchall()

    for opinion in opinions:
        cursor.execute("SELECT text from pros WHERE opinion_id = %s", (opinion['id'],))
        pros = cursor.fetchall()
        opinion['pros'] = pros

    for opinion in opinions:
        cursor.execute("SELECT text from cons WHERE opinion_id = %s", (opinion['id'],))
        cons = cursor.fetchall()
        opinion['cons'] = cons

    json = {
        'product': product,
        'opinions': opinions
    }

    return jsonify(json)

@app.route('/product/<id>/recommendationRatio/')
def recommendation_ratio(id):
    cursor = DB.cursor()

    cursor.execute("SELECT recommendation FROM opinions WHERE product_id=%s", (id,))
    rec = cursor.fetchall()
    cursor.close()

    return jsonify(rec)

@app.route('/product/<id>/opinionsPerStars/')
def opinions_per_stars(id):
    cursor = DB.cursor(dictionary=True)

    cursor.execute("SELECT stars, count(id) AS opinions FROM opinions WHERE product_id=%s GROUP BY stars ORDER BY stars ASC", (id,))
    stars = cursor.fetchall()
    cursor.close()

    return jsonify(stars)
