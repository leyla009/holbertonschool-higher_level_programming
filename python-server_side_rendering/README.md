# Python - Server Side Rendering

## Description
This project focuses on the various ways to render content on the server side using Python. It begins with fundamental string manipulation and graduates to using the **Flask** web framework combined with the **Jinja2** templating engine. You will learn to handle multiple data formats (JSON, CSV, and SQLite) and serve them dynamically through a web interface.

## Learning Objectives
*   Implement manual string templating for file generation.
*   Build and configure a Flask web application.
*   Master Jinja2 syntax for loops, conditionals, and template inheritance.
*   Modularize HTML using `{% include %}` for shared components.
*   Parse data from **JSON** and **CSV** files using Python's built-in libraries.
*   Connect to and query a **SQLite** database within a Flask route.
*   Utilize URL query parameters (`request.args`) to filter and display specific data.
*   Design robust error handling for "File Not Found" and "Invalid Source" scenarios.

## Project Directory Structure

| File | Description |
| --- | --- |
| `task_00_intro.py` | Python function to generate invitation files; handles type checking and missing data. |
| `task_01_jinja.py` | Flask app demonstrating basic routing and modular headers/footers. |
| `task_02_logic.py` | Uses Jinja loops and `if` statements to render items from a JSON file. |
| `task_03_files.py` | Fetches product data from either JSON or CSV based on URL parameters. |
| `task_04_db.py` | Integrated app that adds SQLite support as a third data source. |
| `items.json` | JSON file used for basic list rendering exercises. |
| `products.json` | Product dataset in JSON format. |
| `products.csv` | Product dataset in CSV format. |
| `products.db` | SQLite database file containing the `Products` table. |
| `templates/` | Directory containing all `.html` Jinja templates. |

## Requirements
*   **Python:** 3.8.x or higher.
*   **Flask:** Install via `pip install Flask`.
*   **Style:** All Python code is formatted according to the `pycodestyle` (PEP 8) standard.
*   **Shebang:** Every Python script begins with `#!/usr/bin/python3`.

## Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone <your-repo-url>
    cd holbertonschool-higher_level_programming/python-server_side_rendering
    ```
2.  **Initialize the Database:**
    Before running the SQL task, ensure the database exists:
    ```bash
    python3 -c "import sqlite3; conn = sqlite3.connect('products.db'); cursor = conn.cursor(); cursor.execute('CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL)'); conn.commit(); conn.close()"
```    
