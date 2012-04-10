import operator 
import math
def ThreeDigitFactor_palindro(N):
    """docstring for ThreeDigitFactor_palindro"""
    for i in range(110,int(math.sqrt(899998)),11):
        #print i
        if N%i==0:
            if operator.__and__(N/i>100,N/i<999):
                return i,N/i


def palindro():
    """docstring for palindro"""
    """6 digits palindro number: abccba"""
    N=899998
    a,b,c=0,0,0
    while N>100001:
        N=899998-c*1100-b*10010-a*100001
        c=c+1
        while c==10:
            b=b+1
            c=0
        while b==10:
            a=a+1
            b,c=0,0
        yield N

if __name__ == '__main__':
    for n in palindro():
        if ThreeDigitFactor_palindro(n):
            print ThreeDigitFactor_palindro(n),n
            break

