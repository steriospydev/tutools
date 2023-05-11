from bs4 import BeautifulSoup
import requests
"""
Requirements:
    requests
    bs4
    html5lib
"""


def extract_links(url:str) -> list:
    links = {}
    headers = {
      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
      "accept-language":"en-US,en;q=0.9,it;q=0.8,es;q=0.7",
      "accept-encoding":"gzip,deflate,br",
      "referer":"https://google.com/"
    }
    req = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(req.text, "html5lib")    
    for index, link in enumerate(soup.findAll('a')):
        links[index] = link.get('href')
    return links
