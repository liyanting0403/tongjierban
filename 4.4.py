def number(year):
    for i in range(2010,2021):
        if i % 4 == 0 and i % 100 != 0 or i % 400 ==0:
            print(str(i)+"年共有366天哦！！！")
        else:
            print(str(i)+"年共有365天哦！！！")
def start():
    number(2010)
start()