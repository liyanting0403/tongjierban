num = int(input("请输入一个数字："))
for i in range(1000):
    if num == i:
        print("find")
        break #中断循环，循环不再执行
    print(i)