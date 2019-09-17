"""迭代器
mylist = [1,2,3,4,5,6]
it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))"""

""" 列表生成式，缺点是占内存
mylist = [x for x in range(15)]
print(mylist)
while True:
   pass
mylist = [x * x for x in range(10) if x <6 ]
print(mylist)
"""