#引入模块
import math_operations

num1 = int(input("请输入number1: "))
num2 = int(input("请输入number2: "))

print(math_operations.add(num1, num2))
print(math_operations.multiply(num1, num2))

#引入包
import animals

print(animals.meow())
print(animals.dog.bark())

import sys
print(sys.path)


#引入三方包 request