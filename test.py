# coding: UTF-8
import urllib.request
import re
import json
from bs4 import BeautifulSoup

# def urlToSoup(url):
#     try:
#         response = urllib.request.urlopen(url)
#         html = response.read()
#         soup = BeautifulSoup(html, "html.parser")
#         return soup
#     except:
#         return None

url = "https://movie.douban.com/top250?start=0"
response = urllib.request.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "html.parser")

url_list = []

for url in soup.select(".hd>a"):
    url_list.append(url.attrs["href"])

print(url_list[0])