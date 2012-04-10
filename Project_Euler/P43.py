import string
#def FirstTwoDigits(int_N):
    #if len(str(int_N)>1):
        #return str(int_N[0:2])
    #else:
        #return 0

def NextThreeDigitsNum(str_N):
    if len(str_N)!=len(set(str_N)):
        return []
    array=[]
    for i in string.digits:
        if len(str_N)==2:
            str_N='0'+str_N
        if not(i in str_N):
            array.append(i+str_N[0:2])
    return array

if __name__ == '__main__':
    #initialization
    ini=range(17,1000,17)
    ini=map(str,ini)
    divs=[13,11,7,5,3,2];
    nextthree=map(NextThreeDigitsNum,ini)
    print nextthree
