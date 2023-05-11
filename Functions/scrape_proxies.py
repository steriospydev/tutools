import requests
from random import choice
from bs4 import BeautifulSoup
"""
Requirements:
    requests
    bs4
    html5lib
"""

def get_proxy_ip():
    """Scrape IPs and Ports from sslproxies.org
    Args:
        None
    Returns:
        IP:PORT 
    """
    response = requests.get("https://sslproxies.org/")
    soup = BeautifulSoup(response.content, 'html5lib')
    ip_li = soup.findAll('td')[::8]
    ports_li = soup.findAll('td')[1::8]
    ips = [ip.text for ip in ip_li]
    ports = [port.text for port in ports_li]
    ips = ips[:len(ips)-20]
    ports = ports[:len(ports)-15]
    return choice(ips) +':'+ choice(ports)

print(get_proxy_ip())