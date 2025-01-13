"""
for循环
语法：
    for 变量 in 可迭代对象:
        循环体
"""

for i in range(1,10):
    print(i)

j = 10
while j > 0:
    j -= 1
    if(j == 0):
        print("最后一次啦")
        break


"""
文件控制
语法：
    file = open("文件路径", "模式")
    模式：
        "r"	以只读模式打开文件（文件必须存在）。
        "w"	以写入模式打开文件（会清空文件内容，如果文件不存在会创建一个新文件）。
        "a"	以追加模式打开文件（写入内容追加到文件末尾，不会清空文件）。
        "r+"	以读写模式打开文件（文件必须存在，不会清空内容）。
        "w+"	以读写模式打开文件（会清空文件内容，如果文件不存在会创建一个新文件）。
        "a+"	以读写模式打开文件（写入内容追加到文件末尾，不会清空内容）。
扩展：
    python中关于资源使用（网络连接/数据库/文件等）的最佳实践with，会自动关闭资源，不需要手动写close
"""

file = open("/Users/lujian/temp/test.txt", "r")
try:
    print("read方法：")
    print(file.read())

    print("readline方法：")
    file.seek(0) #指针重置到开头
    print(file.readline())

    print("readlines方法：")
    file.seek(0) #指针重置到开头
    print(file.readlines())
finally:
    file.close()

with open("/Users/lujian/temp/test.txt", "a+") as file1: 
    #默认a+指针会跑到文件最后，所以这边read读不出内容
    file1.read() 
    file1.write("im test\n")

