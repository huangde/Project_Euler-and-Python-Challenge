import Primelist
from P3 import IsPrime

listb=Primelist.primes(1000)
lista=range(-999,1000,2)

def f1(a,b):
    return lambda n:n**2+a*n+b

def Nprime(c):
    n=0
    nprime=0
    while c(n)>0:
        if IsPrime(c(n)):
            n+=1
            nprime+=1
        else:
            break
    return nprime


res=[]
for a in lista:
    for b in listb:
        c=f1(a,b)
        n=Nprime(c)
        # print n,a,b
        res.append((n,a,b))
print max(res)
