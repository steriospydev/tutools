import pyshorteners

def urlshortener(url):
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    return url_short

