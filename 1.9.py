# 0:剪刀 1:石头 2:步
import random
def cp():
    c = random.randint(0,2)
    p = int(input("请输入0-2："))
    print("机器人为：",c)
    if c == 0 and p == 1:
        print("你赢了")
    elif c == 0 and p == 2:
        print("电脑赢了")
    elif c == 0 and p == 0 or c == 1 and p == 1 or c == 2 and p == 2:
        print("平局")
    elif p == 0 and c == 1:
        print("电脑赢了")
    else:
        print("你赢了")
def start():
    cp()
start()
