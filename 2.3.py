def runnian():
    year = int(input("请输入年份>>>"))
    month = int(input("请输入月份>>>"))
    if month == 1:
        print(str(year)+"年"+str(month)+"月有31天")
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0:
            print(str(year)+"年的"+str(month)+"月有29天")
        else:
            print(str(year)+"年的"+str(month)+"月有28天")
    elif month == 3:
        print(str(year)+"年的"+str(month)+"月有31天")
    elif month == 4:
        print(str(year)+"年的"+str(month)+"月有30天")
    elif month == 5:
        print(str(year)+"年的"+str(month)+"月有31天")
    elif month == 6:
        print(str(year)+"年的"+str(month)+"月有30天")
    elif month == 7:
        print(str(year)+"年的"+str(month)+"月有31天")
    elif month == 8:
        print(str(year)+"年的"+str(month)+"月有31天")
    elif month == 9:
        print(str(year)+"年的"+str(month)+"月有30天")
    elif month == 10:
        print(str(year)+"年的"+str(month)+"月有31天")
    elif month == 11:
        print(str(year)+"年的"+str(month)+"月有30天")
    elif month == 12:
        print(str(year)+"年的"+str(month)+"月有31天")
    else:
        print("你是不是傻！！！")
def start():
    runnian()
start()