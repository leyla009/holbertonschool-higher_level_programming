# Python - Abstract Base Classes (ABC)

## Description
This project focuses on advanced Object-Oriented Programming (OOP) concepts in Python. Specifically, it explores the use of Abstract Base Classes (ABCs), the implementation of interfaces, and the concept of "Duck Typing."

## Learning Objectives
By the end of this project, you will be able to:
* Define and use **Abstract Base Classes** to create blueprints for other classes.
* Use the `@abstractmethod` decorator to enforce method implementation in subclasses.
* Understand the concept of **Duck Typing** (if it walks like a duck and quacks like a duck, it is a duck).
* Use the `abc` module to design robust software architectures.

## Requirements
* All files are interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
* All files should end with a new line.
* The first line of all files should be exactly `#!/usr/bin/python3`.
* A `README.md` file at the root of the folder of the project is mandatory.
* Your code should use the `pycodestyle` style (version 2.8.*).
* All modules, classes, and functions must have documentation.

---

## Tasks

### 0. Abstract Animal Class and its Subclasses
Creation of an abstract class `Animal` using the `abc` module.
* **Abstract Method:** `sound()`
* **Subclasses:** `Dog` (returns "Bark"), `Cat` (returns "Meow").

### 1. Shape, Color and ABC
An exercise in multi-level inheritance and abstraction involving geometric shapes and their attributes.

### 2. Duck Typing
Implementing a function that interacts with different objects based on their behavior (methods) rather than their explicit class type.

### 3. Iterators and Generators
Exploring Python's protocol for iteration by creating custom iterator classes and generator functions.

