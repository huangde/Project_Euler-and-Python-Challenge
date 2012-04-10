def fibo_generator():
    a,b=1,1
    while True:
        a,b=b,a+b
        yield a    
if __name__ == '__main__':
    a=fibo_generator()
    counter=1
    while True:
        tmp=a.next()
        counter+=1
        #print counter,tmp
        if (tmp%10**999!=tmp):
            break
    print tmp
    print counter


