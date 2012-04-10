import itertools
if __name__ == '__main__':
    a='0123456789'
    a=itertools.permutations(a)
    count=0
    for i in a:
        count+=1
        #print count,i
        if count==1000000:
            break
    print i

