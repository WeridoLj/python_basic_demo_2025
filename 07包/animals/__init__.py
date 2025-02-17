#__init__py 内容可以为空。但是会把animals目录标识为一个包
from .cat import meow

"""
# 直接import dog 在包里会报错，找不到对应模块

# 使用绝对路径引入
import animals.dog
from animals.dog import bark
from animals import dog
"""

## 使用相对路径引入
from . import dog

