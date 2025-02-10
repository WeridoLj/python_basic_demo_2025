"""
任务1：计算器函数

要求：
	1.定义一个 calculator(a, b, operator) 函数，实现 + - * / 计算。
	2.处理除零错误 ZeroDivisionError。
	3.让用户输入两个数和运算符，调用函数计算结果。
"""
def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        try:
            return a / b
        except ZeroDivisionError:
            return '除法运算时，分母不能为0'
    else:
        return "请输入正确的运算符"

try:
    num1 = int(input("请输入数字1:"))
    num2 = int(input("请输入数字2:"))
    ope = input("请输入运算符:")
    print(calculator(num1, num2, ope))
except ValueError:
    print("请输入正确的数字类型")



"""
任务2：统计单词频率

要求：
	1.让用户输入一段文本。
	2.使用 word_count(text) 统计每个单词出现的次数，返回字典格式 {word: count}。
	3.输出统计结果。
"""
def word_count(text):
    words = text.split(" ")
    wordMap = {}
    for word in words:
        wordMap[word] = wordMap.get(word, 0) + 1
    print(wordMap)
    return wordMap
word_count("hello hello world")


"""
任务3：模拟用户注册
要求：
	1.让用户输入 用户名 和 密码，存入 users.txt 文件（格式：用户名#密码）。
	2.定义 register_user(username, password)，检查用户名是否已存在，如果存在则提示“用户名已存在”。
	3.如果注册成功，提示“注册成功”。
"""
def register_user(username, password):
    try:
        with open("/Users/lujian/temp/users.txt", "a+") as loginFile:
            loginFile.seek(0)
            usersInfo = loginFile.readlines()
            if any(userinfo.split("#")[0] == username for userinfo in usersInfo): #生成器表达式
                    print(f"用户名{username}已被注册，请重试")
            else:
                loginFile.write(username + "#" + password + "\n")
                print("注册成功")
    except FileNotFoundError:
        print("用户数据文件不存在，正在创建新文件...")
        with open("/Users/lujian/temp/users.txt", "w") as loginFile:
            loginFile.write(username + "#" + password + "\n")
            print("注册成功")
username = input("请输入用户名：").strip()
password = input("请输入用户密码：").strip()
register_user(username, password)
