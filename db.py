# coding: UTF-8
import pymysql
import traceback

# 数据库配置
db_host = "193.112.100.48"
db_name = "test"
db_username = "zorichen"
db_password = "123456"
db_charset = "utf8"


# 连接数据库
def getDB():
    try:
        db = pymysql.connect( db_host,db_username,db_password,db_name,charset=db_charset)
        print("连接数据库正常")
        return db
    except:
        print("连接数据库失败")

# 添加方法，防注入
def handleSQL(sql,data):
    db = getDB()
    cursor = db.cursor()
    try:
        cursor.execute(sql,data)
        db.commit()
        print("执行SQL成功")
    except Exception as e:
        print("执行SQL失败：", e)
        db.rollback()
    finally:
        db.close

