import codecs
file = codecs.open("C:/Users/admin/Desktop/rating.json","rb","utf-8")
while True:
    mystr = input("请输入您要查找的数据：")
    while True:
        linestr = file.readline()
        if linestr.find(mystr) != -1:
            print(linestr,end=" ")
        if linestr == None:
            break
