"""file = open("C:/Users/admin/Desktop/liyanting.txt","wb") 读取中文
mystr = '''
 《木兰花令》 纳兰性德  
人生若只如初见，何事秋风悲画扇？
等闲变却故人心，却道故人心易变。
骊山语罢清宵半，泪雨零铃终不怨。
何如薄倖锦衣郎，比翼连枝当日愿！
'''
file.write(mystr.encode("utf-8"))
file.close()"""
file = open("C:/Users/admin/Desktop/liyanting.txt","w")  # 读取英文
mystr = "hello world"
file.write(mystr)
file.close()