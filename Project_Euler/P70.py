def phi(N):
    """docstring for phi"""
    import gcd
    count=0
    for i in range(1,N):
        if gcd.gcd(N,i)==1:
            count+=1
    return count

def Digits(N):
    """docstring for Digits"""
    N=list(str(N))
    N.sort()
    return N

def IsPermutation(N):
    if Digits(N)==Digits(phi(N)):
        return True
    else:
        return False

if __name__ == '__main__':
    for i in range(1,10000000):
        if IsPermutation(i):
            print i,phi(i),i/phi(i)

