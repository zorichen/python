# coding: UTF-8
from movie_db import *
import time

# 获得当前时间
def getCurrentTime():
    timeStamp = int(time.time())
    localTime = time.localtime(timeStamp) 
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime) 
    return strTime

def addMovies(movie_list):
    
    total_num = len(movie_list)
    flag = 0

    # 需要添加电影总数 
    print("总共有" + str(total_num) + "部电影需要添加...")
    
    for movie in movie_list:
        flag += 1
        print( "正在添加第" + str(flag) + "/" + str(total_num) + "部电影..." )
        insertMovie(movie)
        