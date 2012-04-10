def IsPalindromic(n):
    #for i in range(0,len(str(n))/2+1,1):
    #	if str(n)[i]!=str(n)[-1-i]:
    #	    return False
    #return True
    ##########################
    #version 2
    if str(n)==str(n)[::-1]:
	return True
    return False

def NumReverse(n):
    return int(str(n)[::-1])

def IsLychrel(n):
    counter=0
    while counter<50:
	n=n+NumReverse(n)
	if IsPalindromic(n):
	    return False
   	counter=counter+1
    return True

if __name__=="__main__":
    counter=0
    for i in range(1,10001,1):
	if IsLychrel(i):
	    counter=counter+1
    print counter
    
