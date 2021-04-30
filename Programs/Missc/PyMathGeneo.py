from bs4 import BeautifulSoup
import requests
import requests.exceptionsfrom urllib.parse 
import urlsplitfrom urllib.parse 
import urlparsefrom collections 
import deque

url = “https://genealogy.math.ndsu.nodak.edu/”

# a queue of urls to be crawled nextnew_urls 

pre = deque([url])