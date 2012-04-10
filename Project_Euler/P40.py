if __name__ == '__main__':
    inilist=''
    i=0
    while len(inilist)<=1000000+1:
        inilist+=str(i)
        i=i+1
    #print inilist,inilist[12]
    j=1
    prod=1
    while j<=1000000:
        prod=prod*int(inilist[j])
        print j,inilist[j],prod
        j=j*10



