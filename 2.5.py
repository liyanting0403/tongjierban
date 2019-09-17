#while... else
def mima():
    password = input("请输入密码：")
    while password != "123456":
        password = input("密码错误，请重新输入密码：")
    else:
        print("登陆成功")
def start():
    mima()
start()