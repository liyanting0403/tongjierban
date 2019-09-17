import codecs
file = codecs.open("C:\\Users\\admin\\Desktop\\abc.txt","rb","gbk","ignore")
while True:
    mystr = input("请输您要查找的数据：")
    while True:
        line = file.readline()
        if line.find(mystr) != -1:
            print(line,end=" ")
        if line.find == None:
            break
