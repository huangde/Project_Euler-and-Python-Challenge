def recurcycle2(n):
    num=1000
    array=[]
    while(num%n!=0):
	array.append(num%n)
	if array.count(num%n)>1:
	    array.pop()
	    break
      	num=num%n*10
    return array,len(array)

if __name__=="__main__":
    maxcycle=0
    imax=0
    for i in range(2,1000,1):
        array,arrlen=recurcycle2(i)
	#print i,array,arrlen
	if (arrlen>maxcycle):
	    maxcycle=arrlen
	    max    =i
	print maxcycle,imax
