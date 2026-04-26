#!/usr/bin/python3
"""
A simple Flask API providing user management endpoints.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the operational status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the full object for a specific username.
    Returns 404 if the user is not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the dictionary from a POST request.
    Handles validation for JSON validity, missing username, and duplicates.
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # This was the likely cause of the FAIL
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    response = {
        "message": "User added",
        "user": data
    }
    return jsonify(response), 201


if __name__ == "__main__":
    app.run()
