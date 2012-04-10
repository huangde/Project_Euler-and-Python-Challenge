def DigitSum(n):
    sum=0
    for digit in str(n):
	sum+=int(digit)
    return sum

if __name__=="__main__":
    max=0
    #for a in range(100):
    #	for b in range(100):
    #	    if DigitSum(a**b)>max:
    #		max=DigitSum(a**b)
    ##########################################
    #version 2
    myset=set(DigitSum(a**b) for a in range(101) for b in range(101))
   # without 'set' keyword, myset will become a generator!!!!!
    for i in myset:
	if i>max:
	    max=i	
    print max
