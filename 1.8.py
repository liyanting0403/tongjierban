import random
def touyingbi():
    a = random.randint(0,1)
    b = int(input("请输入0或1:"))
   
    if b == a:
        print("you are right")
    else:
        print("you are wrong")
def start():
    touyingbi()
start()