# coding: UTF-8
from getDoubanMovieTop250URL import *
from getMovies import *
from addMovies import *

# 获取豆瓣电影top250的链接列表
url_list = getDoubanMovieTop250URL()
# 获取豆瓣电影top250的电影对象列表
movies = getMovies(url_list)
# 插入数据库
addMovies(movies)