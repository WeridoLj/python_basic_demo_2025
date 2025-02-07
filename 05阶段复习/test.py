"""
任务1：Python 计算器（异常处理 + 循环）
要求：
	•让用户输入两个数字和运算符 (+, -, *, /)，并计算结果。
	•如果用户输入错误（如输入非数字，或者 / 进行除零运算），程序应捕获异常并提示错误信息，要求用户重新输入。
提示：
	•try-except 处理 ValueError 和 ZeroDivisionError
	•while 让用户不断输入，直到输入正确
"""
while True:
    try:
        num1 = int(input("请输入数字1："))
        num2 = int(input("请输入数字2："))
        calculate = input("请输入运算符：")
        if calculate == '+':
            res = num1 + num2
        elif calculate == '-':
            res = num1 - num2
        elif calculate == '*':    
            res = num1 * num2
        elif  calculate == '/':
            res = num1 / num2
        else:
            raise ValueError
        print(f"res = {res}")
        break
    except ValueError:
        print(f"请输入正确的数字和运算符")
    except ZeroDivisionError:
        print(f"分母不能为0")



"""
任务2：记事本应用（文件操作 + 异常处理）
要求：
	•让用户选择：
        1.读取已有记事内容
        2.写入新内容（追加模式）
        3.退出程序
	•处理 FileNotFoundError，如果文件不存在，提示用户创建新文件。
提示：
	•使用 with open("notebook.txt", "a+") as f: 进行文件操作。
	•让用户输入内容后，追加到文件中。
"""
while True:
    order = input("请选择操作指令：\n1.读取已有记事内容\n2.写入新内容（追加模式）\n3.退出程序\n:")
    if order == "3":
        break
    elif order == "1":
        with open("/Users/lujian/temp/test.txt","r") as file:
            print(file.read())
    elif order == "2":
        with open("/Users/lujian/temp/test.txt","a+") as file:
            newContent = input("请输入追加内容:")
            file.write(newContent+"\n")
            file.seek(0)
            print(file.read())



"""
任务3：用户登录系统（文件 + 异常处理）
要求：
	1.让用户注册账号（用户名 + 密码），存入 users.txt 文件。
	2.让用户登录时输入用户名和密码：
	    •如果用户名不存在，提示“用户不存在”。
	    •如果密码错误，提示“密码错误”。
	    •如果正确，则显示“登录成功”。
	3.处理 FileNotFoundError，如果 users.txt 不存在，则创建它。

提示：
	•读取用户数据时，使用 strip() 清除换行符。
	•注册时，把 用户名:密码 存入 users.txt。
	•登录时，逐行检查用户名和密码是否匹配。
"""
while True:
    order = input("请选择操作指令：\n1.用户注册\n2.用户登陆\n3.退出:")
    if order == "1" :
        username = input("请输入用户名：").strip()
        password = input("请输入用户密码：").strip()
        with open("/Users/lujian/temp/users.txt", "a+") as loginFile:
            loginFile.seek(0)
            usersInfo = loginFile.readlines()
            if any(userinfo.split("#")[0] == username for userinfo in usersInfo): #生成器表达式
                    print(f"用户名{username}已被注册，请重试")
                    sameNameFlag = True
            else:
                loginFile.write(username + "#" + password + "\n")
    elif order == "2":
        username = input("请输入用户名：").strip()
        password = input("请输入用户密码：").strip()
        try:
            with open("/Users/lujian/temp/users.txt", "r") as loginFile:
                usersInfo = loginFile.readlines()
                userMap = {userinfo.split("#"[0]):userinfo.split("#")[1] for userinfo in usersInfo} #字典表达式，在下面可以用map哈希查找，时间复杂度O(1)
                if username not in userMap:
                     print("用户不存在")
                elif userMap[username] == username:
                    print ("登陆成功")
                else:
                    print("账号或密码错误")
        except FileNotFoundError:
            print("用户不存在，请先进行用户注册")
    elif order == "3":
        break