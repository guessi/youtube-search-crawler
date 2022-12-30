#!/usr/bin/env python3

from search import search

from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def api():
    query = request.args.get("q", "youtube")
    app.logger.debug(query)
    return search(escape(query))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8080)
