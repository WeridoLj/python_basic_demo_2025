#任务1：编写一个程序，模拟简单的购物车功能：
#1.用户可以反复输入商品，输入"q"结束
#2.最后输出用户输入的所有商品名称
products = []
while True:
    product = input("请输入商品名，按q退出：")
    if product == 'q':
        break
    if product.strip() == '':
        print("商品输入不能为空")
        continue
    products.append(product)
print(f"你输入的商品有：{','.join(products)}")


#任务2：九九乘法表（复习进阶版）
# 在屏幕上打印九九乘法表，要求：
# 1.左对齐显示（每列宽度相同）
# 2.行与行之间用空行分隔
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i*j}", end="\t")
    print("\n")