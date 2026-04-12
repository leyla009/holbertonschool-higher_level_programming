# Python - Inheritance

## Description
This project is part of the Higher Level Programming curriculum and focuses on the implementation and mechanics of **Inheritance** in Python. It covers how to extend class functionality, use built-in introspection tools, and manage class hierarchies.

## Learning Objectives
By the end of this project, you are expected to be able to explain:
* What is a superclass, baseclass, or parentclass.
* What is a subclass.
* How to list all attributes and methods of a class or instance.
* How to inherit a class from another.
* How to define a class with multiple base classes.
* How to override a method or attribute inherited from the base class.
* The purpose of `isinstance`, `issubclass`, `type`, and `dir` functions.

## Requirements
* **Environment:** Ubuntu 20.04 LTS
* **Language:** Python 3.8.5
* **Style Guide:** `pycodestyle` (version 2.8.*)
* **Documentation:** All modules, classes, and functions must have a docstring.

## Tasks

### [0. Lookup](./0-lookup.py)
* **Goal:** Write a function that returns the list of available attributes and methods of an object.
* **Prototype:** `def lookup(obj):`
* **Constraints:** No modules allowed.

## Usage
To test the implementation of task 0:
```python
#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

class MyClass:
    my_attr = 5

print(lookup(MyClass))
