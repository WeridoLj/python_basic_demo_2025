#任务1：异常捕获
#编写一个程序，模拟一个简单的计算器：
# 	1.用户输入两个数字和一个运算符（如 +、-、*、/）
# 	2.根据运算符输出结果
# 	3.如果用户输入无效数据或除数为零，捕获并提示错误信息
try:
    res = None
    num1 = int(input('num1 : '))
    num2 = int(input('num2 : '))
    calculate = input('操作符 : ')
    if calculate == '+':
        res = num1 + num2
    elif calculate == '-':
        res = num1 - num2
    elif calculate == '*':
        res = num1 * num2
    elif calculate == '/':
        res = num1 / num2
    else:
        raise ValueError('操作符输入错误')
except ValueError:
    print(f"输入内容格式错误")
except ZeroDivisionError as e:
    print(f"分母不能是0，异常信息：{e}")
finally:
    if res is not None:
        print(f"系统计算完成,结果={res}")
    else:
        print(f"系统计算失败,结果={res}")


#任务2：文件读取与异常处理
#编写一个程序，模拟一个简单的计算器：
#   1.尝试打开一个文件并读取其内容
# 	2.如果文件不存在，捕获异常并提示用户
# 	3.在 finally 块中打印一条提示信息，例如“操作结束”
try:
    with open("/Users/lujian/temp/test11.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("文件不存在")
finally:
    print("操作结束")
    

#任务3：自定义异常
# 	1.编写一个程序，验证用户输入的密码长度：
# 	•如果密码少于 8 个字符，抛出自定义异常 PasswordTooShortError
# 	•提示用户重新输入密码，直到符合条件为止
from PasswordTooShortError import PasswordTooShortError

password = None
while password == None or len(password) < 8:
    try:
        password = input("请输入密码:")
        if len(password) < 8:
            raise PasswordTooShortError
    except PasswordTooShortError as e:
        print("密码小于8位，请重新输入")
    else:
        print("密码输入完毕")
        break

