import math
import itertools
import Primelist

if __name__ == '__main__':
    num=[]
    a=Primelist.primes(9999)
    a=[i for i in a if i>1000]
    for i in a:
        b=itertools.permutations(str(i))
        for c in b:
            d=[map(int,x) for x in c]
            if d[0]!=0:
                k=d[0][0]*1000+d[1][0]*100+d[2][0]*10+d[3][0]
                if k in a:
                    num.append(k)
                    a.pop(a.index(k))
                    #print count,k
        if len(set(num))>=3:
            tmp=itertools.combinations(num,2)
            for comb in tmp:
                #print comb,sum(comb),num
                if sum(comb)/2 in num:
                    print num,comb,sum(comb)/2
        num=[]
