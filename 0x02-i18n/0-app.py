#!/usr/bin/env python3
""" simple flask app """
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello_world():
    """a basic app"""
    return render_template('0-index.html')

if __name__ == "__main__":
    app.run()
