if __name__ == '__main__':
    #calculate maximum number from permutations
    m=lambda x:int(max(list(str(x)))*len(list(str(x))))
    #calculate the set of all digits:
    s=lambda x:map(int,str(x))
    count=0
    j=345
    while count<5:
        count=0
        for i in range(j,int(m(j**3)**(1.0/3))+1):
            a,b=s(i**3),s(j**3)
            a.sort()
            b.sort()
            if a==b:
                count+=1
        print j,count
        j+=1
    print j-1
