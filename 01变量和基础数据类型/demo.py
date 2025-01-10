"""
基础数据类型
"""
name="张三"
age=12
print(f"name={name},age={age}")
#python中不允许int和字符串拼接
print(f"name={name},age="+str(age))

"""
数据类型转换
"""
number="123"
print(int(number)+1) #print(number+1)会直接报错


"""
运算符计算
"""
x=2
y=3
print(x+y,x-y,x*y,x/y)
print(x//y,x**y,x%y)


"""
输入和输出
"""
uname=input("input your name:")
uage=int(input("input your age"))
print(f"uname={uname},uage={uage}")



