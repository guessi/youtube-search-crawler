# YouTube Search Results Crawler

Simple script for parsing search results from YouTube

# Usage

Setup Requirements

```
$ pip3 install -r requirements.txt
```

Start a flask service with youtube search

```
$ ./main.py

* Serving Flask app "main" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

Usage
```
$ curl http://localhost:5000\?q\=五月天 | jq

$ {
  "data": [
    {
      "source_id": "0AZYWl0gFiM",
      "thumbnail": "https://i.ytimg.com/vi/0AZYWl0gFiM/hqdefault.jpg",
      "title": "ADELE 21 - The Best of Adele - Adele Greatest Hits (FULL ALBUM)"
    },
    {
      "source_id": "YQHsXMglC9A",
      "thumbnail": "https://i.ytimg.com/vi/YQHsXMglC9A/hqdefault.jpg",
      "title": "Adele - Hello"
    },
    {
      "source_id": "OHXjxWaQs9o",
      "thumbnail": "https://i.ytimg.com/vi/OHXjxWaQs9o/hqdefault.jpg",
      "title": "Adele at the BBC: When Adele wasn't Adele... but was Jenny!"
    },
    {
      "source_id": "qPkPx5ol4NE",
      "thumbnail": "https://i.ytimg.com/vi/qPkPx5ol4NE/hqdefault.jpg",
      "title": "Adele Adele Ade Adele Bass-Aranan Müzik::.[*_*].::Spektra::."
    },
    {
      "source_id": "KOwxb9s9GjY",
      "thumbnail": "https://i.ytimg.com/vi/KOwxb9s9GjY/hqdefault.jpg",
      "title": "Bang La Decks - Aide (Official Audio)"
    },
    {
      "source_id": "PQM3XUhiXbQ",
      "thumbnail": "https://i.ytimg.com/vi/PQM3XUhiXbQ/hqdefault.jpg",
      "title": "EXTENDED version of \"When Adele Wasn't Adele\" | Adele: Live in London"
    },
    {
      "source_id": "rYEDA3JcQqw",
      "thumbnail": "https://i.ytimg.com/vi/rYEDA3JcQqw/hqdefault.jpg",
      "title": "Adele - Rolling in the Deep"
    },
    {
      "source_id": "fAJUMzY5iVc",
      "thumbnail": "https://i.ytimg.com/vi/fAJUMzY5iVc/hqdefault.jpg",
      "title": "The Best of Adele - Adele Greatest Hits (FULL ALBUM)"
    },
    {
      "source_id": "Ri7-vnrJD3k",
      "thumbnail": "https://i.ytimg.com/vi/Ri7-vnrJD3k/hqdefault.jpg",
      "title": "Adele - Set Fire To The Rain (Live at The Royal Albert Hall)"
    },
  ]
}
```

## License

[MIT](LICENSE)
