money = 0
def search(name):
    list = ["妞妞","花花","萌萌","宁宁","肉肉"]
    if name not in list:
        chong()
    else:
        print("该好友已存在")
def chong():
    global money
    if money >=1000:
        print("已偷偷帮您加回好友")
        re = input("是否删除好友[y/n]")
        if re =='y':
            print("该好友不得删除")
        money -= 1000
        f = open("C:/Users/Asus/Desktop/tt.txt","w",encoding = "utf-8") 
        f.write(str(money))
        f.close()
    else:
        print("费用不够呀，请充值点吧！！！")
        res = input("是否愿意充值？[y/n]")
        if res == "y":
            print("正在跳转微信支付，请稍等一会会儿！！")
            money1 = float(input("请充值："))
            money += money1
            chong()         #自己调用自己  递归
        else:
            print("GoogBye!!")
def start():
    name = input("添加好友，请输入昵称>>>")
    search(name)
start()