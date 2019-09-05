# coding: UTF-8
from getMovieInfo import *
from datetime import datetime
def getMovies(url_list):
    flag = 0
    movies = []

    # 抓取电影信息
    for url in url_list:
        flag += 1
        starttime = datetime.now()
        try:
            movie = getMovieInfo(url)
            movies.append(movie)
            endtime = datetime.now()
            spendtime = (endtime - starttime).seconds
            print( "抓取第" + str(flag) + "部电影成功...耗时：" + str(spendtime) + "秒..." )
        except Exception as e:
            endtime = datetime.now()
            spendtime = (endtime - starttime).seconds
            print( "抓取第" + str(flag) + "部电影失败...耗时：" + str(spendtime) + "秒..." + "\n" + "报错信息：" + str(e) )
    
    return movies