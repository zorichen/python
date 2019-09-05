# coding: UTF-8
from getMovieInfo import *
from testTool import *

def getDoubanTop250():
    base_url = "https://movie.douban.com/top250?start="
    url_list = []

    print( "开始时间:" + getCurrentTime() )

    # 获得250个链接
    for i in range(0,250,25):
        url = base_url + str(i)
        soup = urlToSoup(url)
        for url in soup.select(".hd>a"):
            url_list.append(url.attrs["href"])
    return url_list