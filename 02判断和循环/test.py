#任务1：编写一个程序，输入一个分数，判断它的等级
try:
    score = int(input("请输入一个分数:"))
    if score >= 90:
        print("优秀")
    elif 80 <= score < 90:
        print("良好")
    elif 60 <= score < 80:
        print("及格")
    else:
        print("不及格")
except ValueError:
    print("分数请输入数字")


#任务1：使用for循环打印乘法表（九九表）
"""
示例：
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
...
"""
for i in range(1,10):
    res = [i * j for i in range(1,10) for j in range(1,10)]

