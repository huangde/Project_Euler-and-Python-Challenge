import math
def Primelist(N):
    """finding all the prime numbers less than N"""
    """slow version"""
    init_list=range(3,N,2)
    j=0
    while j!=len(init_list):
        for i in init_list[j+1:]:
            if i%init_list[j]==0:
                k=i
                while k in init_list:
                    init_list.pop(init_list.index(k))
                    k=k+init_list[j]
        j+=1
    return init_list

def sieve_Primelist(N):
    """fast sieve version"""
    init_list=range(3,N,2)
    for i in range(int(N**0.5+1)):
        if init_list[i]:
            if N>init_list[i]**2:
                start_num=init_list[i]**2
                for j in range(start_num,N,init_list[i]*2):
                    if j in init_list:
                        init_list[init_list.index(j)]=0
    return [x for x in init_list if x]

def primes(n): 
    """the fastest version"""
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]
