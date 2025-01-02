#任务1：编写一个简单的脚本，输入两个数字，计算它们的和、差、积、商，并输出结果。
try:
    num1=int(input("num1："))
    num2=int(input("num2："))

    quotient=0
    if num2==0:
        print("num2不能为0")
    else:
        quotient=num1/num2
    sum=num1+num2
    difference=num1-num2
    product=num1*num2
    print(f"num1={num1}, num2={num2}, sum={sum}, difference={difference}, product={product}, quotient={quotient}")
except ValueError:
    print("请输入数字！")


#任务2：编写一个小程序，提示用户输入一个整数，判断该数是奇数还是偶数，并输出结果。
try:
    num=int(input("请输入一个整数："))
    quotient=num%2
    if quotient==0:
        print(f"{num}是偶数")
    else:
        print(f"{num}是奇数")
except ValueError:
    print("请输入数字！")