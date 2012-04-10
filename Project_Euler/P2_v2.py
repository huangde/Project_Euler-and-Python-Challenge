def fibo(n):
    if n==1 or n==2:
        return n
    else:
	return fibo(n-1)+fibo(n-2)

def fibo_gen(imax):
    i=2
    while fibo(i)<imax:
        yield fibo(i)
        i+=3

if __name__=='__main__':
    sum=0
    imax=4000000
    generator=fibo_gen(imax)
    for i in generator:
	#print i
	sum=sum+i
    print sum
