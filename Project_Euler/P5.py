import math
def IsPrime(N):
    """docstring for Prime"""
    if isinstance(N,(int,long)):
        if N==1:
            return False
        if N==2: 
            return True
        if N%2==0:
            return False
        for x in range(3,int(math.sqrt(N))+1,2):
            #print x,N,N%x
            if N%x==0:
                return False
                break
        return True
    else:
        print 'input must be a integer'
        return False


def MaxFactor(N):
    """docstring for MaxFactor"""
    if N==2:
        return N
    if N%2==0:
        return N/2
    else:
        for x in range(3,int(math.sqrt(N))+1,2):
            if N%x==0:
                return N/x
                break
        return N

def PrimeFactors(Num):
    array=[]
    MaxFac=MaxFactor(Num)
    array.append(Num/MaxFac)
    while IsPrime(MaxFac)==False:
        Num=MaxFac
        MaxFac=MaxFactor(Num)
        array.append(Num/MaxFac)
        #print Num,MaxFac
    array.append(MaxFac)
    return array

if __name__ == '__main__':
    ans=2**4*3**2*5*7*11*13*17*19
