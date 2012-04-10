import math
import Primelist
import P3

def IsSquareNum(N):
    """docstring for SquareNum"""
    tmp=int(math.sqrt(N))
    if N%tmp==0 and N/tmp==tmp:
        return True
    else:
        return False

def CG_conjecture(N):
    """docstring for CG_conjecture"""
    a=Primelist.primes(N)
    for i in a[1:]:
        if IsSquareNum((N-i)/2):
            #print N,'=',i,'+','2*',math.sqrt((N-i)/2),'**2'
            return True
    return False


if __name__ == '__main__':
    N=7
    while True:
        N=N+2
        if P3.IsPrime(N)==False:
            if CG_conjecture(N)==False: 
                break
    print N
