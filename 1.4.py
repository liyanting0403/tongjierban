def num():
    a = float(input("请输入a的值>>>"))
    b = float(input("请输入b的值>>>"))
    c = float(input("请输入c的值>>>"))
    g = float(b * b - 4* a * c)
    r1 = (-b + g ** 0.5) / 2* a
    r2 = (-b - g ** 0.5) / 2* a
    if g > 0:
        print(r1,r2)
    elif g == 0:
        print(r1)
    else:
        print("不存在")
def start():
    num()
start()
