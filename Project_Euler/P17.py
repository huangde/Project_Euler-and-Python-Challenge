def num2word(N):
    """docstring for num2word"""
    n2wdict={1:'one',2:'two',3:'three',\
     4:'four',5:'five',6:'six',\
     7:'seven',8:'eight',9:'nine',\
     10:'ten',11:'eleven',12:'twelve',\
     13:'thirteen',14:'fourteen',15:'fifteen',\
     16:'sixteen',17:'seventeen',18:'eighteen',\
     19:'nineteen',20:'twenty',30:'thirty',\
     40:'forty',50:'fifty',60:'sixty',\
     70:'seventy',80:'eighty',90:'ninety',1000:'onethousand'}
    letterNum=''
    if N in n2wdict:
        letterNum+=n2wdict[N]
        return letterNum
    if(N%100==0):
        letterNum+=n2wdict[N/100]+'hundred'
        return letterNum
    elif(N>100):
        letterNum+=n2wdict[N/100]+'hundred'+'and'
    N=N%100
    if(N%10==0):
        letterNum+=n2wdict[N]
        return letterNum
    elif(N/10==1):
        letterNum+=n2wdict[N]
        return letterNum
    elif(N/10!=0):
        m=int(str(N)[-1])
        N=N-m
        letterNum+=n2wdict[N]+n2wdict[m]
    else:
        letterNum+=n2wdict[N]
    return letterNum



if __name__ == '__main__':
    letterNum=0
    for i in range(1,1001,1):
        letterNum+=len(num2word(i))
        print i,num2word(i),letterNum
