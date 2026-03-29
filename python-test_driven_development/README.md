# Python - Test-driven development

## Description
This project focuses on the importance of testing in Python. Instead of just writing code, we write tests first (or alongside) using the `doctest` module to ensure our functions handle edge cases, incorrect types, and unexpected inputs gracefully.

## Learning Objectives
* Why unit testing is important
* How to write a `doctest`
* How to execute `doctest`
* How to look for edge cases
* The difference between LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission)

## Tasks

| File | Description |
| --- | --- |
| [0-add_integer.py](./0-add_integer.py) | Function that adds 2 integers with strict type checking. |
| [tests/0-add_integer.txt](./tests/0-add_integer.txt) | Doctest for the `add_integer` function. |

## Requirements
* Allowed editors: `vi`, `vim`, `emacs`
* All files interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* All files should end with a new line
* The first line of all files should be exactly `#!/usr/bin/python3`
* All modules, classes, and functions must have documentation (`__doc__`)
* A `tests` folder must be present at the root of the project
* All tests should be executed by: `python3 -m doctest ./tests/*`
