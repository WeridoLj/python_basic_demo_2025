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


#任务2：使用for循环打印乘法表（九九表）
"""
示例：
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
...
"""
for i in range(1,10):
    for j in range(1,i+1):
        res = i * j
        print(f"{i} * {j} = {res}", end="\t")
    print()


#任务3：输入一个整数，输出从1到这个整数中所有奇数的平方，并存储到列表中（使用列表推导式）
num1 = 19
num2 = [x ** 2 for x in range(1, num1) if x %2 != 0]
print(num2)
