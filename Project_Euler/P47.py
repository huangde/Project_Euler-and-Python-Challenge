import math
import divisors
#TODO:extremly slow!!!
if __name__ == '__main__':
    tmp=[]
    Consecutive_len=4
    b=1
    while len(tmp)<Consecutive_len:
        b+=1
        if len(set(divisors.Primedivisors(b)))==Consecutive_len:
            tmp.append(b)
            print tmp
        else:
            tmp=[]
    print tmp
