def sum_sq(N):
    """docstring for sq_sum"""
    sum=0
    for i in range(1,N+1,1):
        sum=sum+i**2
    return sum

def sq_sum(N):
    sum=0
    for i in range(1,N+1,1):
        sum=sum+i
    sum=sum**2
    return sum

if __name__ == '__main__':
    a=sum_sq(100)
    b=sq_sum(100)
    print a,b,b-a
