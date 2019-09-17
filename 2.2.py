"""n = 0
while n ** 2 <12000:
    n += 1
    print(n)"""


def wanquan():
    for i in range(1,10000):
        num = 0
        for j in range(1,i):
            if i % j ==0:
                num += j
        if i == num:
           print(i)
def start():
    wanquan()
start()
