#!/usr/bin/env python3

import click
import requests

from bs4 import BeautifulSoup


@click.command()
@click.option('-k', '--keyword', 'keyword', help='keyword for search',
        default='Adele Hello', show_default=True)
def ytSearch(keyword):
    print(f'Search for \"{keyword}\"...\n')

    search_endpoint = 'https://www.youtube.com/results'
    search_query_uri = search_endpoint + '?&gl=US&hl=en&sp=CAMSAhAB&search_query='
    result = requests.get(search_query_uri + keyword)
    html_content = BeautifulSoup(result.text, 'html.parser')
    items = html_content.find_all('div', {'class': 'yt-lockup-content'})

    count = 0
    print(">>>")
    for item in items:
        count = count + 1
        try:
            print('Title: ' + item.h3.a['title'])
            temp_list_element = item.select('div div.yt-lockup-meta ul li')
            print('Date:  ' + temp_list_element[0].text)
            print('View:  ' + temp_list_element[1].text)
            print('Link:  https://www.youtube.com' + item.h3.a['href'])
        except e:
            print(e)

        print(">>>")

    print('Results: ' + str(count))

if __name__ == '__main__':
    ytSearch()
