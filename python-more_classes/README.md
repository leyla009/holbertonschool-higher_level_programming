# Python - More Classes and Objects

## Project Description
This directory contains the second phase of the Object-Oriented Programming (OOP) curriculum. While the previous project focused on basic instantiation and data encapsulation, this project explores:
- Class Attributes
- Static Methods
- Class Methods
- Special "Magic" Methods that control how objects are represented and deleted.

## Learning Objectives
By completing the projects in this directory, you will understand:
- **Class Attributes vs. Instance Attributes:** Knowing when to share data across all instances.
- **Magic Methods:**
  - `__str__`: Providing a user-friendly string representation.
  - `__repr__`: Providing an "official" string representation for debugging.
  - `__del__`: Handling object destruction.
- **Data Abstraction & Encapsulation:** Refined use of properties and setters.
- **Static Methods (`@staticmethod`):** Methods that don't need access to the instance or class.
- **Class Methods (`@classmethod`):** Methods that belong to the class rather than the instance.

## Requirements
- **Interpreter:** All files are executed on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- **Style:** All code adheres to the [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) (version 2.8.*) standard.
- **Documentation:** Modules, classes, and methods are fully documented with docstrings.
- **Executability:** All files are created with `#!/usr/bin/python3` and are executable.

## Directory Structure
| File | Description |
|---|---|
| 0-rectangle.py | Defines an empty class Rectangle |
| 1-rectangle.py | Adds width and height attributes with validation |
| 2-rectangle.py | Adds area and perimeter methods |
| 3-rectangle.py | Implements `__str__` to print the rectangle with `#` |
| 4-rectangle.py | Implements `__repr__` for a developer-ready string representation |
| 5-rectangle.py | Implements `__del__` to print a message when deleted |
| 6-rectangle.py | Introduces a class attribute `number_of_instances` |
| 7-rectangle.py | Introduces a class attribute `print_symbol` |
| 8-rectangle.py | Adds a static method `bigger_or_equal` |
| 9-rectangle.py | Adds a class method `square` that returns a new Rectangle instance |

## Usage
### Clone the repository:
bash
git clone https://github.com/holbertonschool-higher_level_programming.git
cd python-more_classes

### Execution: Run the provided main files to test the classes:
bash
chmod +x 0-main.py
./0-main.py
