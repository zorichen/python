# coding: UTF-8
from getDoubanMovieInfo import *
from datetime import datetime
import time

# 获得当前时间
def getCurrentTime():
    timeStamp = int(time.time())
    localTime = time.localtime(timeStamp) 
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime) 
    return strTime

# 获取电影详细信息，输入url列表，输出movie对象列表
def getMovies(url_list):

    total_num = len(url_list)
    flag = 0
    movie_list = []

    # 需要抓取电影总数 
    print("总共有" + str(total_num) + "部电影需要抓取...")
    
    # 抓取电影信息
    for url in url_list:
        # 计数
        flag += 1
        # 计时
        starttime = datetime.now()
        try:
            movie = getDoubanMovieInfo(url)
            movie_list.append(movie)
            endtime = datetime.now()
            spendtime = (endtime - starttime).seconds
            print( "抓取第" + str(flag) + "/" + str(total_num) + "部电影成功...耗时：" + str(spendtime) + "秒..." )
        except Exception as e:
            endtime = datetime.now()
            spendtime = (endtime - starttime).seconds
            print( "抓取第" + str(flag) + "/" + str(total_num) + "部电影失败...耗时：" + str(spendtime) + "秒..." + "\n" + "报错信息：" + str(e) )
    
    return movie_list