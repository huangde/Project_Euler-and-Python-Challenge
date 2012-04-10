#def fibo(nmax):
    #"""docstring for fibo"""
    #array=[]
    #if nmax==1:
        #array.append(1)
    #if nmax==2:
        #array.append(1)
        #array.append(2)
    #if nmax>2:
        #array.append(1)
        #array.append(2)
        #tail=2
        #i=3
        #while i<nmax:
            #array.append(i)
            #tail=tail+1
            #i=array[tail-1]+array[tail-2]
    #return array            

def fibo(nmax):
    """docstring for fibo"""
    array=[]
    a,b=1,2
    array.append(a)
    while b<nmax:
        array.append(b)
        a,b=b,a+b
    return array

if __name__ == '__main__':
    sum=0
    imax=4000000
    array=fibo(imax)
    for i in range(1,len(array)+1,3):
        sum=sum+array[i]
        print array[i] 
    print sum
