Number = input('number:>>')
		if len(Number) > 3:
		    print('[!] Error, The lenghts must be Three!!')
		else:
		    bai = int(Number[0])
		    shi = int(Number[1])
		    ge = int(Number[2])
		    if bai ** 3 + shi **3 + ge **3 == int(Number):
		        print('水仙花')
		    else:
		        print('不是')
