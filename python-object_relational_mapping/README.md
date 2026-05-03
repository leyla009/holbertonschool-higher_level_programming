# Python - Object-Relational Mapping

This project bridges the gap between **Databases** and **Python**. It explores how to connect to a MySQL database from a Python script and how to use **SQLAlchemy**, a popular Python SQL toolkit and Object-Relational Mapper (ORM).

## 📋 Project Overview
The goal of this project is to abstract the database interaction. Instead of writing raw SQL queries, you will learn to interact with database tables as if they were Python objects.

## 🛠️ Technologies & Tools
* **Language:** Python 3.8.x
* **Database:** MySQL 8.0
* **Libraries:** `MySQLdb`, `SQLAlchemy`
* **OS:** Ubuntu 20.04 LTS

## 📂 Learning Objectives
* How to connect to a MySQL database from a Python script.
* How to `SELECT` rows from a table using the `MySQLdb` module.
* How to `INSERT` rows into a table using the `MySQLdb` module.
* What **ORMapping** means.
* How to map a Python Class to a MySQL table.
* How to use SQLAlchemy to query, insert, update, and delete data.

## 🚀 Key Tasks

### Part 1: MySQLdb
Interacting with the database using raw SQL queries passed through the `MySQLdb` cursor.
* Listing all states from the database.
* Filtering states by user input (safe from SQL injection).

### Part 2: SQLAlchemy
Transitioning to the ORM approach for better maintainability and abstraction.
* Defining a `State` class and linking it to the `states` table.
* Using a `Session` to interact with the database.
* Performing CRUD (Create, Read, Update, Delete) operations without writing SQL.

## ⚠️ Requirements
* All files are interpreted on Ubuntu 20.04 LTS using `python3`.
* Code should follow the `pycodestyle` (version 2.8.*) guidelines.
* All modules, classes, and functions must have documentation.
