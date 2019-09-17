import random
def num():
    num1 = random.randint(1,10)
    num2 = int(input("请输入数字："))
    while num2 != num1:
        if num2 > num1:
            print("big")
        else:
            print("small")
        num2 = int(input("数字错误，请重新输入数字:"))
    else:
        print("right")
def start():
    num()
start()