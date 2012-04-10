def Collatz_series(n):
    array=[n]
    while n!=1:
	if n%2==0:
	    n=n/2
	    array.append(n)
	else:
	    n=3*n+1
	    array.append(n)
    return array

if __name__=="__main__":
    max,imax=0,0
    for i in range(2,1000000,1):
        print i, len(Collatz_series(i))
        if len(Collatz_series(i))>max:
            max,imax=len(Collatz_series(i)),i

