# YouTube Search Results Crawler

[![Docker Stars](https://img.shields.io/docker/stars/guessi/youtube-search-crawler.svg)](https://hub.docker.com/r/guessi/youtube-search-crawler/)
[![Docker Pulls](https://img.shields.io/docker/pulls/guessi/youtube-search-crawler.svg)](https://hub.docker.com/r/guessi/youtube-search-crawler/)
[![Docker Automated](https://img.shields.io/docker/automated/guessi/youtube-search-crawler.svg)](https://hub.docker.com/r/guessi/youtube-search-crawler/)

Simple service for search results from YouTube

# Usage
 
### Run with Docker
 
```
$ docker pull guessi/youtube-search-crawler:latest
$ docker run -d -p 5000:5000 guessi/youtube-search-crawler:latest
$ curl http://localhost:5000\?q\=Adele%20Hello
```

### Developer Build
 
Setup Requirements

```
$ pip3 install -r requirements.txt
```

Start Flask App with YouTube Search

```
$ python3 ./main.py

* Serving Flask app "main" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Search Locally

```
$ curl http://localhost:5000\?q\=Adele%20Hello | jq '.'

{
  "data": [
    {
      "source_id": "0AZYWl0gFiM",
      "thumbnail": "https://i.ytimg.com/vi/0AZYWl0gFiM/hqdefault.jpg",
      "title": "ADELE 21 - The Best of Adele - Adele Greatest Hits (FULL ALBUM)"
    },
    ...
    ...
    ...
  ]
}
```

## License
 
[MIT](LICENSE)
