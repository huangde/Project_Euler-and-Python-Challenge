import divisors
import itertools
if __name__ == '__main__':
    abundant_num=[]
    Sumof2abunds=[]
    for i in range(1,28124,1):
        if sum(divisors.prop_divs(i))>i:
            abundant_num.append(i)
    ini=range(0,28124,1)
    for i in ini:
        for j in abundant_num[0:i/2+1]:
            if i-j in abundant_num:
                print i,'=',j,'+',i-j
                Sumof2abunds.append(i) 
                break
    print sum(set(ini)-set(Sumof2abunds))
