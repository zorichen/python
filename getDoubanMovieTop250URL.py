# coding: UTF-8
import urllib.request
from bs4 import BeautifulSoup

# 读取url转化成BeautifulSoup对象
def urlToSoup(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        return soup
    except:
        return None
        
# 获取豆瓣电影top250榜单的链接，无输入，输出url列表
def getDoubanMovieTop250URL():
    base_url = "https://movie.douban.com/top250?start="
    url_list = []

    # 获得250个链接
    for i in range(0,250,25):
        url = base_url + str(i)
        soup = urlToSoup(url)
        for movie in soup.select(".hd>a"):
            url_list.append(movie.attrs["href"])
    return url_list

# 测试

url_list = getDoubanMovieTop250URL()
print(url_list)