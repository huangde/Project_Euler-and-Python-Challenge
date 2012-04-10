def fibo(n):
    if n==1 or n==2:
        return n
    else:
	return fibo(n-1)+fibo(n-2)

if __name__=='__main__':
    sum=0
    i=2
    imax=4000000
    while fibo(i)<imax:
	#version 1
        if fibo(i)%2==0:
	    sum=sum+fibo(i)
    	    print fibo(i)
    	i=i+1
    print sum	
