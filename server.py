# Importing necessary modules
from flask import Flask, jsonify

# Creating a Flask application instance
app = Flask(__name__)

# Defining a route for the root URL ("/") that returns a simple message
@app.route("/")
def hello_world():
    # Creating a dictionary representing the response body
    body = {
        "message": "Hello World",
    }
    # Returning the response body
    return body

# Defining a route for "/jsonify" that returns a JSON response
@app.route("/jsonify")
def test_message():
    # Creating a message string
    message = "This is a test"
    # Using Flask's jsonify function to convert the message into a JSON response
    return jsonify(message)
