#!/usr/bin/python3
import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    """Reads data from products.json."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    """Reads data from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, ValueError):
        pass
    return products

def read_sql():
    """Reads data from products.db (SQLite)."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        # This row_factory allows accessing columns by name like a dictionary
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append(dict(row))
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    return products

@app.route('/products')
def display_products():
    """Renders product data from JSON, CSV, or SQL sources."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validation for supported sources
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    # Select data source based on query parameter
    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sql()

    # Filtering logic by ID
    if product_id:
        try:
            pid = int(product_id)
            products = [p for p in products if p.get('id') == pid]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
