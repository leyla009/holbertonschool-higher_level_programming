# SQL Introduction

Fundamentals of **SQL** and relational databases.

## Key Terms
* **SQL**: Structured Query Language.
* **DDL**: Data Definition (Structure).
* **DML**: Data Manipulation (Records).
* **Relational DB**: Data organized in tables, rows, and columns.

## Basic Syntax
| Action | SQL Command |
| :--- | :--- |
| **List All** | `SELECT * FROM users;` |
| **Add** | `INSERT INTO users (id, name, age) VALUES (2, "Betty", 30);` |
| **Filter** | `SELECT * FROM users WHERE age > 21;` |
| **Modify** | `UPDATE users SET name = "Holberton" WHERE id = 89;` |
| **Remove** | `DELETE FROM users WHERE id = 89;` |

> **Warning:** Always use `WHERE` with `UPDATE` or `DELETE` to avoid data loss.
