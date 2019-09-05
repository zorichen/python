# coding: UTF-8
from db import *

# 添加电影
def insertMovie(movie):
   # 预处理语句
   sql = "INSERT INTO movie ( name,localname,year,director,screenwriter,actor,genre,country,language,released,runtime,main_pic,douban,douban_rating,douban_top250,imdb ) VALUES ( %(name)s,%(localname)s,%(year)s,%(director)s,%(screenwriter)s,%(actor)s,%(genre)s,%(country)s,%(language)s,%(released)s,%(runtime)s,%(main_pic)s,%(douban)s,%(douban_rating)s,%(douban_top250)s,%(imdb)s )"
   # 插入数据
   handleSQL(sql,movie)
