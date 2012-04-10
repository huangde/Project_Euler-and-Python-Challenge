import math
def triangular_counts(p):
    count=[]
    #for m in range(int(math.sqrt(p/4))-1,int(math.sqrt(3*p/4))+1,1):
        #if p%(2*m)==0:
            #n=p/m/2-m
            #if n<m and n>0:
                #print m,n
                #a=m**2-n**2
                #b=2*m*n
                #c=m**2+n**2
                #print a,b,c,a**2+b**2==c**2
    #real number version(slow)
    for m in range(p/4-1,p/2+1,1):
        if ((p/2)-m)**2%m==0:
            n=((p/2)-m)**2/m
            if n<m and n>0:
                #print m,n
               # a=m-n
                #b=2*int(math.sqrt(m*n))
                c=m+n
                count.append(c)
    return len(set(count))
                #print a,b,c,a**2+b**2==c**2


if __name__ == '__main__':
    max_count=0
    idx=0
    for i in range(8,1000,2):
        if triangular_counts(i)>max_count:
            idx=i
            max_count=triangular_counts(i)
    print idx,max_count
