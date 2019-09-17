import random
def sum_(sum):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    if num1 + num2 ==sum:
        print("you are right")
    else:
        print("you are wrong")
def start():
    sum = int(input("请输入num的值："))
    sum_(sum)
start()

    
    