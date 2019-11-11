# coding: UTF-8
import urllib.request
import re
import json
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

# 从豆瓣抓取电影详细信息，传入url，返回movie对象
def getDoubanMovieInfo(url):
    # 通过url获得BeautifulSoup对象
    soup = urlToSoup(url)

    # 处理豆瓣电影信息
    
    # 名称
    try:
        name_temp = soup.find("span", property="v:itemreviewed").get_text()
        if (" " in name_temp):
            name_temp = name_temp.split(" ",1)
            name = name_temp[0]
            localname = name_temp[1]
        else:
            name = name_temp
            localname = None
    except:
        name = None
        localname = None

    # 年份
    try:
        year = soup.find("span", class_="year").get_text().strip("()")
    except:
        year = None
    
    # 导演
    try:
        director = []
        director_list = soup.find_all("a", rel="v:directedBy")
        for item in director_list:
            director.append(item.get_text())
        director = str(director)
    except:
        director = None

    # 编剧
    try:
        screenwriter = []
        temp = [ item for item in soup.find("span", text="编剧").next_siblings ]
        for item in temp[-1].find_all("a"):
            screenwriter.append(item.get_text())
        screenwriter = str(screenwriter)
    except:
        screenwriter = None

    # 主演
    try:
        actor = []
        actor_list = soup.find_all("a", rel="v:starring")
        for item in actor_list:
            actor.append(item.get_text())
        actor = str(actor)
    except:
        actor = None

    # 类型
    try:
        genre = []
        genre_list = soup.find_all("span", property="v:genre")
        for item in genre_list:
            genre.append(item.get_text())
        genre = str(genre)
    except:
        genre = None

    # 制片国家/地区
    try:
        country = soup.find("span", text="制片国家/地区:").next_sibling
    except:
        country = None

    # 语言
    try:    
        language = soup.find("span", text="语言:").next_sibling
    except:
        language = None

    # 上映时间
    try:
        released = []
        released_list = soup.find_all("span", property="v:initialReleaseDate")
        for item in released_list:
            released.append(item.get_text().strip())
        released = str(released)
    except:
        released = None

    # 片长
    try:
        runtime = soup.find("span", property="v:runtime").get_text()
    except:
        runtime = None

    # 封面图
    try:
        main_pic = soup.find("a", class_="nbgnbg").img.attrs["src"]
    except:
        main_pic = None

    # 豆瓣 subject_id
    try:
        douban_id = url.strip("https://movie.douban.com/subject/")
    except:
        douban_id = None
    # 豆瓣评分
    try:
        douban_rating = soup.find("strong", property="v:average").get_text()
    except:
        douban_rating = None       
        
    # 豆瓣 top250
    try:
        douban_top250 = soup.find("span", class_="top250-no").get_text().strip("No.")
    except:
        douban_top250 = None         

    # IMDb id
    try:
        imdb_id = soup.find("a", text=re.compile("tt")).get_text()
    except:
        imdb_id = None
    
    # 拼接成电影信息json
    movie = {
        "name": name,
        "localname": localname,
        "year": year,
        "director": director,
        "screenwriter": screenwriter,
        "actor": actor,
        "genre": genre,
        "country": country,
        "language": language,
        "released": released,
        "runtime": runtime,
        "main_pic": main_pic,
        "douban_id": douban_id,
        "douban_rating": douban_rating,
        "douban_top250": douban_top250,
        "imdb_id": imdb_id
    }
    
    return movie

# # 测试
# movie = getDoubanMovieInfo("https://movie.douban.com/subject/1851857/")
# print(movie)