"""mylist = ([x for x in range(100)]) #  类型 <class 'list'> 列表
print(type(mylist))"""

# mylist = (x for x in range(1000))#  类型 <class 'generator'> 生成器 会大大的节约内存
# print(type(mylist))
"""print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))
print(next(mylist))"""
# for it in  mylist:       # 循环
 #   print(it)

def go():
    print(1)
    yield 1
    print(2)
    yield 2
print(type(go()))