from search import search

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def api():
    return search(request)

if __name__ == "__main__":
        app.run()
