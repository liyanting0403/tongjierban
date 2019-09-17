def geshu():
    zhengshu = 0
    fushu = 0
    sum = 0
    count = 1
    while count != 0:
        count = int (input("请输入数字：："))
        if count > 0:
            zhengshu += 1
        elif count <0:
            fushu += 1
        else:
            pass
        sum += count
    print("负数个数为： %d"%fushu)
    print("正数个数为： %d"%zhengshu)
    pingjun = sum / (zhengshu + fushu)
    print("平均值为： %f"%pingjun)
def start():
    geshu()
start()