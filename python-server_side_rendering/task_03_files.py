#!/usr/bin/python3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    """Reads products from products.json."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv():
    """Reads products from products.csv."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id and price to appropriate types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except (FileNotFoundError, ValueError):
        pass
    return products

@app.route('/products')
def display_products():
    """Renders product data based on source and id query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Check for valid source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # Load data based on source
    if source == 'json':
        products = read_json()
    else:
        products = read_csv()

    # Filter by ID if provided
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
