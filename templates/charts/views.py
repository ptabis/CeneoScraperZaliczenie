from templates import app
from flask import render_template, redirect, request
from Database import DB

@app.route('/charts/<id>/')
def charts(id):
    cursor = DB.cursor(dictionary=True)
    cursor.execute("SELECT p.*\
         FROM products p\
         WHERE p.id=%s", (id,))
    product = cursor.fetchall()
    cursor.close()

    return render_template("charts.html", subname=f"Wykresy produktu - {product[0]['id']} - {product[0]['name']}", mod="charts", product=product[0])