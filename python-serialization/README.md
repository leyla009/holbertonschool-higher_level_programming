# Python - Serialization

## Description
This project explores the concept of **Serialization** and **Deserialization**. Serialization is the process of converting a data structure or object state into a format that can be stored (for example, in a file or memory buffer) or transmitted and reconstructed later in the same or another computer environment.

In this directory, we focus on using the `json` module to handle data persistence for Python dictionaries.

## Learning Objectives
* Understand what serialization and deserialization are.
* Learn how to use the `json` module to convert Python objects to JSON strings and files.
* Learn how to recreate Python objects from JSON data.
* Practice file handling in Python using the `with` statement.

## Requirements
* All files interpreted on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* Code should follow the `pycodestyle` (version 2.8.*) style guide.
* All modules, classes, and functions must have documentation.

## Tasks

### 0. Basic Serialization
Create a module `task_00_basic_serialization.py` that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

**Functions:**
* `serialize_and_save_to_file(data, filename)`: Saves the dictionary `data` into `filename` in JSON format.
* `load_and_deserialize(filename)`: Reads `filename` and returns the reconstructed Python dictionary.

## Usage
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data = {"name": "John Doe", "age": 30}
serialize_and_save_to_file(data, 'data.json')

new_data = load_and_deserialize('data.json')
print(new_data)
