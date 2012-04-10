if __name__ == '__main__':
    from math import *
    n=287
    while True:
        y=n*(n+1)/2
        if (1+sqrt(1+24*y))%6==0:
            print n,y
            break
        n+=2
