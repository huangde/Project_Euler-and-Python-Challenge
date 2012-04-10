def Digits(N):
    """docstring for Digits"""
    N=list(str(N))
    N.sort()
    return N


if __name__ == '__main__':
    for num in range(200000):
        tmp=num
        digittmp=Digits(tmp)
        for i in range(1,7):
            if Digits(tmp*i)!=digittmp:
                break
            if i==6:
                print tmp
            
