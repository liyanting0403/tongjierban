def num(n):
    for n in range(100):
        a = n*(3*n-1)/2
        print(int(a),end=' ')
        if n%10 == 0:   
            print('\n') 
def start():
    num(100)
start()