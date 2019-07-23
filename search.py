import re
import requests

from bs4 import BeautifulSoup
from flask import abort, jsonify


def parse_source_id(href_str):
    source_id = ""
    pattern = re.compile(r'.*v=(?P<source_id>.*)')
    match = pattern.match(href_str)
    if match:
        source_id = match.group("source_id")

    return source_id


def parse_thumbnail(thumbnail_element):
    if thumbnail_element[0].has_attr("data-thumb"):
        thumbnail = thumbnail_element[0]["data-thumb"]
    elif thumbnail_element[0].has_attr("src"):
        thumbnail = thumbnail_element[0]["src"]
    # elimiate unncessary part
    pattern = re.compile(r'(?P<url>.*)\.jpg.*')
    match = pattern.match(thumbnail)
    if match:
        thumbnail = match.group("url") + ".jpg"

    return thumbnail


def search(request):
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
        source_id = parse_source_id(item.h3.a['href'])
        thumbnail = parse_thumbnail(tb_item.select('img'))

        # TBD meta elements
        # we don't need now, so comment it
        # temp_list_element = item.select('div div.yt-lockup-meta ul li')
        # print('Date:  ' + temp_list_element[0].text)
        # print('View:  ' + temp_list_element[1].text)

        # check result
        if source_id == "" or thumbnail == "" or title == "":
            abort(500)

        video = dict(
            title=title,
            source_id=source_id,
            thumbnail=thumbnail,
        )
        data.append(video)

    return jsonify(dict(data=data))
