"""
函数基础语法：
    def 函数名(参数1, 参数2, ...):
        "函数的文档字符串（可选）"
        函数体（代码）
        return 返回值（可选）
"""

def name(name):
    print(f"{name}")

inputName = input("please input your name:")
name(inputName)



"""
Python 支持多种参数类型：
	1.位置参数
	2.默认参数
	3.关键字参数
	4.不定长参数（*args 和 **kwargs）
"""
def add(a, b=50):
    return a / b

def getSum(*nums):
    return sum(nums)

#1.位置参数
print("位置参数：")
print(add(1,2))

#2.默认参数
print("默认参数：")
print(add(1))
print(add(a = 1))

#3.关键字参数
print("关键字参数：")
print(add(a=2, b=1))

#4.不定长参数
print("不定长参数：")
print(getSum(1,2,3))



"""
Python 作用域：
"""
x = 10  #全局变量

def test1():
    x = 5  #局部变量（与全局 x 不同）
    print("局部变量 x =", x)

test1() 
print("全局变量 x =", x)  #全局变量未变

def test2():
    global x 
    x = 11  #修改全局变量，要先声明
    print("局部变量 x =", x)

test2() 
print("全局变量 x =", x)  #全局变量未变



