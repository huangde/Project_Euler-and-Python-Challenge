def Primedivisors(N):
    """return the list of Primedivisors for natural number N"""
    import Primelist
    import math
    import itertools
    import P3
    primediv=[]
    div_num=1
    divs=[1,N]
    if P3.IsPrime(N)==True:
        #return ([],2,divs)
        return []
    a=Primelist.primes(N/2)
    #return primedivisors
    while(N!=1):
        for i in a: 
            while N%i==0:
                N=N/i
                primediv.append(i)
    #return divisors number
    #for i in set(primediv):
        #div_num=div_num*(primediv.count(i)+1)
    ##return divisors
    #for i in range(1,len(primediv)+1,1):
        #b=itertools.combinations(primediv,i)
        #for j in b:
            #prod=1
            #for k in j:
                #prod=prod*k
    #        divs.append(prod)

    #return (primediv,div_num,set(divs))
    return primediv

#def d(N):
    #"""return sum of divisor less than N"""
    ## this version really slow!!!
    #(a,b,c)=Primedivisors(N)
#    return sum(c)-N

def d(N):
    import math
    f=0
    for i in range(1,int(math.sqrt(N))+1,1):
        if N%i==0:
            f+=i
            f+=N/i
    return f-N

def div_num(N):
    """determine divisors number of N--fast version"""
    import math
    count=0
    for i in range(1,int(math.sqrt(N))+1,1):
        if N%i==0:
            count+=2
    return count

def prop_divs(N):
    """docstring for divs"""
    import math
    divlist=[1]
    for i in range(2,int(math.sqrt(N))+1,1):
        if N%i==0:
            divlist+=i,N/i
    return set(divlist)

if __name__ == '__main__':
    result=[]
    finalresult=0
    for i in range (2,10000,1):
        if d(d(i))==i:
            if i!=d(i):
                tmp=(i,d(i))
                result.append(tmp)
    print set(result)
    for i in result:
        finalresult+=sum(i)
    print finalresult/2

