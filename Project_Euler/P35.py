import Primelist
import P3

def RingRotate(N):
    results=[]
    N=str(N)
    for i in range(len(N)):
        N=N[1:]+N[0]
        results.append(N)
    return results

def cyclic(N):
    """docstring for cyclic"""
    results=[]
    if len(str(N))==1:
        return [N]

    for i in str(N):
        if int(i) not in [1,3,7,9]:
            return []

    return map(int,RingRotate(N))

def cyclicPrime(N):
    if cyclic(N)==[]:
        return []
    for i in cyclic(N):
        if not(P3.IsPrime(i)):
            return []
    return N 

if __name__ == '__main__':
    prims=Primelist.primes(1000000)
    result=[]
    for i in prims:
        if cyclicPrime(i):
            result.append(i)
    print result,len(result)
