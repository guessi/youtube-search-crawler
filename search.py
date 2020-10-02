#!/usr/bin/env python3

import json
import random
import re
import requests
import requests_random_user_agent
import time

from bs4 import BeautifulSoup
from flask import abort, jsonify


def search(request):
    q = ""
    request_json = request.get_json()
    if request.args and 'q' in request.args:
        q = request.args.get('q')
    elif request_json and 'q' in request_json:
        q = request_json['q']

    if len(q) <= 0:
        abort(400)

    sp = 'EgIQAQ%253D%253D'  # search preference(sp): video
    endpoint = 'https://www.youtube.com/results'
    uri = endpoint + '?sp=' + sp + '&search_query=' + q

    random.seed(time.time())

    searched = requests.get(uri)
    soup = BeautifulSoup(searched.text, 'html.parser')
    time.sleep(random.random())

    token = 'window\["ytInitialData"\] ='  # noqa
    search_results_raw = soup.find(
        'script',
        string=re.compile(token)
    ).string.strip()

    ytInitialData = search_results_raw.split(';')[0][len(token)-1:]
    ytInitialData_json = json.loads(ytInitialData)

    items = ytInitialData_json['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']  # noqa

    data = []
    for item in items:
        try:
            video_info = item['videoRenderer']

            video_id = video_info['videoId']
            title = video_info['title']['runs'][0]['text']
            publish = video_info['publishedTimeText']['simpleText']
            length = video_info['lengthText']['simpleText']
            thumbnails = video_info['thumbnail']['thumbnails']
            thumbnail = thumbnails[0]['url'].split('?')[0]

            video = dict(
                title=title,
                publish=publish,
                video_id=video_id,
                thumbnail=thumbnail,
                length=length,
            )

            data.append(video)
        except KeyError:
            continue

    return jsonify(dict(data=data))
