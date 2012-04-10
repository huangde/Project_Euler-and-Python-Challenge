import Primelist
import P3

def TruncatablePrime(N):
    """docstring for TruncatablePrime"""
    N=str(N)
    tmplist=[]
    for i in range(1,len(N)):
        tmplist.append(N[i:])
        tmplist.append(N[0:len(N)-i])
    #print tmplist
    tmplist=map(int,tmplist)
    for TruncatedNum in tmplist:
        if not(P3.IsPrime(TruncatedNum)):
            return False
    return True

if __name__ == '__main__':
    inilist=Primelist.primes(1000000)
    result=[]
    for i in inilist:
        if TruncatablePrime(i):
            print i
            result.append(i)
    print sum(result[4:]),len(result)-4
