import time

# 获得当前时间
def getCurrentTime():
    timeStamp = int(time.time())
    localTime = time.localtime(timeStamp) 
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", localTime) 
    return strTime

# 存储数据
def save(content,filename):
    try:
        file = open(filename, "a")
    except Exception as e:
        file = open(filename, "w")
    file.write(content)
    file.close()

# 验证文件类型
def check(content):
    print("----------正在检查变量的类型和长度---------")
    print( "文件类型是：" + str(type(content)) )
    print( "文件长度是：" + str(len(content)) )
    isPrint = input("是否输出结果，打印到屏幕按1，输出到文件按2，不输出按其他任意键" + "\n")
    if isPrint == "1":
        print(content)
    elif isPrint == "2":
        save(content,"./check.txt")
    else:
        print("---操作结束---")