#!/usr/bin/python3
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    """Reads items from a JSON file and renders them in a template."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Access the 'items' list from the dictionary
            items_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback if file is missing or corrupted
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
