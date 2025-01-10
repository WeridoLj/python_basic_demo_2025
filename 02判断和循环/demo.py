"""
判断
"""
num = int(input("请输入一个数字："))
if num > 0:
    print(f"正数")
elif num < 0:
    print(f"负数")
else:
    print(f"0")


"""
循环
"""
for i in range(1,6):
    print(i)

num = 10
while num > 0:
    print(num)
    num -= 1


"""
列表推导式
[表达式 for 元素 in 可迭代对象 if 条件]
"""
#生成一个包含1到10到平方的列表
res1 = [x ** 2 for x in range(1,11)]
print(res1)

res2 = [x ** y for x in range(1,11) for y in range(1,11)]
print(res2)

res3 = [i * j for i in range(1,10) for j in range(1,10)]
print(res3)