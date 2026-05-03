# SQL - More Queries

This directory focuses on advanced SQL concepts, specifically **Data Control Language (DCL)** and complex data retrieval using various **JOIN** types.

## 🛡️ Data Control Language (DCL)
DCL allows for the management of user permissions and security within the database environment[cite: 1].
* **GRANT**: Provides specific access privileges to a user[cite: 1].
* **REVOKE**: Removes previously granted access privileges[cite: 1].

### Permission Capabilities
* **Database Level**: Granting read/write access to an entire database[cite: 1].
* **Table Level**: Granting specific access (e.g., `SELECT`, `INSERT`) to individual tables[cite: 1].
* **Constraint Note**: While `INSERT` can be granted alone, `DELETE` permissions generally require `SELECT` access so users can identify specific records[cite: 1].

## 🔗 JOIN Operations
Joining tables allows for the combination of rows from two or more tables based on a related column.

| Join Type | Description |
| :--- | :--- |
| **INNER JOIN** | Returns records that have matching values in both tables[cite: 1]. |
| **LEFT JOIN** | Returns all records from the left table and matched records from the right[cite: 1]. |
| **RIGHT JOIN** | Returns all records from the right table and matched records from the left[cite: 1]. |
| **FULL OUTER JOIN** | Returns all records when there is a match in either left or right table[cite: 1]. |

> **Note:** Terms like `IN LEFT`, `TOP`, or `FULL INNER` are not valid SQL join types[cite: 1].

## 🛠️ Usage
Files in this directory contain SQL scripts designed to be executed in a MySQL environment to manage permissions and perform complex data queries.
