#猜数字:第一关总共10轮,每一个100分. 
# 由电脑随机产生两个数字,让用户输入这两个数字的和. 
# 最后看是进入第二关还是’Game Over’

import random
def youxi():
    count = 0
    for i in range(5):
        num1 = random.randint(0,5)
        num2 = random.randint(0,5)
        print(num1,num2)
        num3 = int(input("请输入num1+num2 == "))
        if num3 == num1+num2:
            print("please continue")
            count+=200
        else:
            print("error,please continue")

    if count == 1000:
        print('开始第二关')
    else:   
        print('Game Over.')

def start():
    youxi()
start()