from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    body = {
        "message": "Hello World",
    }
    return body

@app.route("/jsonify")
def test_message():
    message ="This is a test"
    return jsonify(message)