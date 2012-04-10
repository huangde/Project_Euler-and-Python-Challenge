import P3
if __name__ == '__main__':
    N=1
    sum=0
    while N<2000000:
        if P3.IsPrime(N)==True:
            sum=sum+N
            #print N,sum
        N=N+1
