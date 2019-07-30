from flask import Flask, escape, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    d = { "msg": "Hello World" }
    return jsonify(d)

