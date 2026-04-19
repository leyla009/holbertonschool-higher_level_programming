# Python - Input/Output

## Description
This project focuses on handling files in Python. It covers reading from and writing to files, using the `with` statement for context management, and working with JSON for data serialization and deserialization.

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone:
* Why Python programming is awesome
* How to open a file
* How to write text in a file
* How to read the full content of a file
* How to read a file line by line
* How to move the cursor in a file
* How to make sure a file is closed after reading
* What is and how to use the `with` statement
* What is JSON
* What is serialization
* What is deserialization
* How to convert a Python data structure to a JSON string
* How to convert a JSON string to a Python data structure

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the `pycodestyle` style (version 2.8.*)
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 0. Read file
Write a function that reads a text file (UTF8) and prints it to stdout:
* Prototype: `def read_file(filename=""):`
* You must use the `with` statement
* You don’t need to manage file permission or file doesn't exist exceptions.
* File: `0-read_file.py`

### 1. Write to a file
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:
* Prototype: `def write_file(filename="", text=""):`
* You must use the `with` statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* File: `1-write_file.py`

### 2. Append to a file
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
* Prototype: `def append_write(filename="", text=""):`
* If the file doesn’t exist, it should be created
* File: `2-append_write.py`

### 3. To JSON string
Write a function that returns the JSON representation of an object (string):
* Prototype: `def to_json_string(my_obj):`
* File: `3-to_json_string.py`

### 4. From JSON string to Object
Write a function that returns an object (Python data structure) represented by a JSON string:
* Prototype: `def from_json_string(my_str):`
* File: `4-from_json_string.py`
