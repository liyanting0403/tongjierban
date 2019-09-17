def number():
    a = int(input("请输入第一个整数："))
    b = int(input("请输入第二个整数："))
    c = int(input("请输入第三个整数："))
    d = [a,b,c]
    d.sort()
    print(d)
def start():
    number()
start()