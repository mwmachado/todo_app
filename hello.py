from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route("/<path:name>")
def hello_name(name):
    return f"Hello, {name}"
    #return f"Hello, {escape(name)}!"