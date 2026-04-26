# RESTful API Development

This directory contains the implementation of a REST API, focusing on standard web communication protocols and the Flask framework.

## 1. HTTP vs. HTTPS
* **HTTP (Port 80):** Data is sent in plain text. Faster but vulnerable to eavesdropping.
* **HTTPS (Port 443):** Data is encrypted via **SSL/TLS**. Ensures security, data integrity, and server authentication.

## 2. Communication Structure

### HTTP Request
* **Method:** Action to perform (GET, POST, etc.).
* **Path:** The URL/Endpoint (e.g., `/api/users`).
* **Headers:** Metadata (e.g., `Content-Type: application/json`).
* **Body:** Data being sent (used in POST/PUT).

### HTTP Response
* **Status Code:** Numeric code indicating the result (e.g., 200, 404).
* **Headers:** Metadata about the response.
* **Body:** The resource data (JSON, HTML, etc.).

## 3. Essential Methods & Status Codes

| Method | Purpose | Use Case |
| :--- | :--- | :--- |
| **GET** | Retrieve | Fetching data from a resource. |
| **POST** | Create | Sending data to create a new resource. |
| **PUT** | Update | Replacing an existing resource. |
| **DELETE** | Remove | Deleting a specific resource. |

| Status Code | Meaning | Scenario |
| :--- | :--- | :--- |
| **200 OK** | Success | Request completed successfully. |
| **201 Created** | Success | A new resource was successfully created. |
| **400 Bad Request** | Client Error | Invalid syntax or missing data in request. |
| **404 Not Found** | Client Error | The requested endpoint does not exist. |
| **500 Internal Error**| Server Error | Unexpected failure on the server side. |

## 4. Tasks Summary
* **`task_02_http_main.py`**: Basic HTTP server using standard libraries.
* **`task_03_http_server.py`**: Routing and handling multiple endpoints.
* **`task_04_flask.py`**: Building a REST API using the **Flask** framework.
* **`task_05_basic_auth.py`**: Securing endpoints with basic authentication.

## 5. Usage
1.  **Install dependencies**: `pip install Flask`
2.  **Run a task**: `python3 task_04_flask.py`
3.  **Test**: Access `http://127.0.0.1:5000/` via browser or `curl`.
