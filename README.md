# YouTube Search Results Crawler

Simple service for search results from YouTube

### Developer Build

Setup Requirements

```
$ pip3 install -r requirements.txt
```

Start Flask App with YouTube Search

```
$ python3 ./main.py

* Serving Flask app 'main' (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on all addresses.
  WARNING: This is a development server. Do not use it in a production deployment.
* Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

Search Locally

```
$ curl "http://127.0.0.1:8080?q=Adele%20Hello" | jq '.'

{
  "data": [
    {
      "length": "6:07",
      "publish": "6 年前",
      "thumbnail": "https://i.ytimg.com/vi/YQHsXMglC9A/hq720.jpg",
      "title": "Adele - Hello",
      "video_id": "YQHsXMglC9A"
    },
    {
      "length": "4:57",
      "publish": "1 年前",
      "thumbnail": "https://i.ytimg.com/vi/be12BC5pQLE/hqdefault.jpg",
      "title": "Adele - Hello (Lyrics)",
      "video_id": "be12BC5pQLE"
    },
    ...
    ...
    ...
  ]
}
```

## License

[MIT](LICENSE)
