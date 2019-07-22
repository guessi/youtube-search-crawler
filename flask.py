import re
import requests

from bs4 import BeautifulSoup
from flask import Flask, request, abort
app = Flask(__name__)

@app.route("/")
def search():
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    q = ""
    request_json = request.get_json()
    if request.args and 'q' in request.args:
        q = request.args.get('q')
    elif request_json and 'q' in request_json:
        q = request_json['q']

    if q == "":
        abort(400)

    endpoint = "https://www.youtube.com/results"
    # sp=video
    uri = endpoint + "?sp=EgIQAQ%253D%253D&search_query=" + q

    result = requests.get(uri + q)
    html_content = BeautifulSoup(result.text, 'html.parser')
    items = html_content.find_all('div', {'class': 'yt-lockup-content'})
    tb_itmes = html_content.find_all('div', {'class': 'yt-lockup-thumbnail'})

    data = []
    for idx in range(len(items)):
        item = items[idx]
        tb_item = tb_itmes[idx]

        # find title
        title = item.h3.a['title']

        # find video id
        source_id = ""
        pattern = re.compile(r'.*v=(?P<source_id>.*)')
        print(item.h3.a['href'])
        match = pattern.match(item.h3.a['href'])
        if match:
            source_id = match.group("source_id")

        # find thumbnail
        thumbnail = ""
        thumbnail_element = tb_item.select('img')
        if thumbnail_element[0].has_attr("data-thumb"):
            thumbnail = thumbnail_element[0]["data-thumb"]
        elif  thumbnail_element[0].has_attr("src"):
            thumbnail = thumbnail_element[0]["src"]

        # check result
        if source_id == "" or thumbnail == "" or title == "":
            abort(500)

        video = dict(
            title=title,
            source_id=source_id,
            thumbnail=thumbnail,
        )
        data.append(video)

    return dict(data=data)

if __name__ == "__main__":
        app.run()
