"""file = open("C:/Users/admin/Desktop/liyanting.txt","r")  读取英文
mystr = file.read()
print(mystr)
file.close()"""
#file = open("C:/Users/admin/Desktop/aaa.txt","wb")
#mystr = """
#《木兰花令》 纳兰性德  
#人生若只如初见，何事秋风悲画扇？
#等闲变却故人心，却道故人心易变。
#骊山语罢清宵半，泪雨零铃终不怨。
#何如薄倖锦衣郎，比翼连枝当日愿！ 
"""
file.write(mystr.encode("utf-8"))
file.close"""

file = open("C:/Users/admin/Desktop/aaa.txt","rb")
mystr = file.read()
print(mystr.decode("utf-8"))
file.close()
