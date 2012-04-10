import P3

def Prime_Generator():
    n=3
    while True:
        if P3.IsPrime(n):
            yield n
        n=n+2
