import Primelist
if __name__ == '__main__':
    sum=0
    a=Primelist.primes(1000000)
    for i in a:
        sum+=i
        if sum in a: 
            print sum
        if sum>1000000:
            break
