#!/usr/bin/env python3

from search import search

from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def api():
    return search(request)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
