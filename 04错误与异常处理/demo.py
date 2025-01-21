"""
异常处理
基本语法：
    try:
        # 可能引发异常的代码
    except 异常类型 as 异常对象:
        # 处理异常的代码
"""
try:
    num = int(input("please input a number:"))
except ValueError as e:
    print(e)
else:
    print("输入成功")
finally:
    print("finallly")   


from CustomError import CustomError
try:
    pwd = input("请输入密码")
    if len(pwd) <= 6:
        raise CustomError("密码不能小于6")
except CustomError:
    print("密码长度不能小于6位")