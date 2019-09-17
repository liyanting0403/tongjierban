def week():
    a = int(input("请输入一周内的那一天："))
    if a == 0:
        print("今天是星期日")
    elif a == 1:
        print("今天是星期一")
    elif a == 2:
        print("今天是星期二")
    elif a == 3:
        print("今天是星期三")
    elif a == 4:
        print("今天是星期四")
    elif a == 5:
        print("今天是星期五")
    else:
        print("今天是星期六")
    day = int(input("请输入未来的天数："))
    day1 = day + a
    if day1 >= 7:
        day2 = day1 % 7
        print("未来那天是星期",day2)
    else:
        print("未来那天是星期",day1)
def start():
    week()
start()

