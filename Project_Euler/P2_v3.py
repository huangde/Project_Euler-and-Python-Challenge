def fibo(n):
    array=[]
    if n==1 or n==2:
        return n 
    else:
        return fibo(n-1)+fibo(n-2)

def fibo_gen():
    i=2
    while True:
        yield fibo(i)
        i+=3

if __name__=='__main__':
    sum=0
    imax=4000000
    generator=fibo_gen()
    for i in generator:
	if i<imax:
	    print i
	    sum=sum+i
	else:
	    break
    print sum
